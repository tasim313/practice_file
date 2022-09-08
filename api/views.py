import json
import re

from requests.exceptions import HTTPError

import psycopg2
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utill import *

from rest_framework.views import APIView

from datetime import timedelta
import datetime
from accounts.models import Appointment
from accounts.serializers import AppointmentSerializer

from django.conf import settings

from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView
from .models import Help
from .serializers import HelpSerialiser


@api_view(["POST"])
def persionApi(request):
    BAHMNI_API_BASE_URL = settings.BAHMNI_API_BASE_URL
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/person"
    payload = request.data
    print("payload", payload["names"][0])
    headers = {"content-type": "application/json"}
    r = requests.post(url, auth=("superman", "Admin123"), data=json.dumps(payload), headers=headers, verify=False)
    return Response(r.json())


@api_view(["POST"])
def personUpdateApi(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/person/469f6217-370a-4335-8116-94ac3317dd9b"
    payload = request.data
    headers = {"content-type": "application/json"}
    r = requests.post(url, auth=("superman", "Admin123"), data=json.dumps(payload), headers=headers, verify=False)
    return Response(r.json())


# @api_view(["GET"])
# def get_radilogy(request, patient_identyfier):
#     try:
#         image_url_list = []
#         obsDatetime_list = {}
#         # GAN203006
#         url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/patient?q=" + patient_identyfier + "&v=default&limit=1"
#         uuid_result = requests.get(url, auth=("superman", "Admin123"), verify=False)
#         if uuid_result:
#             patient_uuid = uuid_result.json()["results"][0]["uuid"]
#             url = (
#                     settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/encounter?encounterType=81f57a25-3f10-11e4-adec-0800271c1b75&patient="
#                     + patient_uuid
#                     + "&v=custom:(uuid,provider,visit:(uuid,startDatetime,stopDatetime),obs:(uuid,concept:(uuid,name),groupMembers:(id,uuid,obsDatetime,value,comment)))"
#             )
#             r = requests.get(url, auth=("superman", "Admin123"), verify=False)
#             # results = r.json()['results'][0]['obs']
#             # for i in results:
#             #     value = (i['groupMembers'][0]['value']).replace('image_url100','')
#             #     x = f"https://bnopenmrs.accelx.net/document_images/{value}"
#             #     image_url_list.append(x)
#             result_list = r.json()["results"]
#             for j in range(0, len(result_list)):
#                 results = r.json()["results"][j]["obs"]
#                 for i in results:
#                     value = (i["groupMembers"][0]["value"]).replace("image_url100", "")
#                     x = f"{settings.BAHMNI_API_BASE_URL}/document_images/{value}"
#                     image_url_list.append(x)
#                     obsDatetime = i["groupMembers"][0]["obsDatetime"]
#                     date_data = {x: obsDatetime[:10]}
#                     obsDatetime_list.update(date_data)
#             context = {
#                 "success": True,
#                 "radiology_images": image_url_list,
#                 "obsDatetime_list": obsDatetime_list,
#             }

#         return Response(context)
#     except Exception as Ex:
#         context = {"success": False, "radiology_images": "No result found"}
#         return Response(context)



@api_view(["GET"])
def get_radilogy(request, patient_uuid):
    
    try:
        url = "https://openemr.accelx.net/openmrs/ws/rest/v1/encounter?encounterType=81f57a25-3f10-11e4-adec-0800271c1b75&patient="+ patient_uuid +"&v=custom:(uuid,provider,visit:(uuid,startDatetime,stopDatetime),obs:(uuid,concept:(uuid,name),groupMembers:(id,uuid,obsDatetime,value,comment)))"
        uuid_result = requests.get(url, auth=("superman", "Admin123"), verify=False)
    #     print(uuid_result.json())
        image_domain_link = "https://openemr.accelx.net/document_images/"

        image_url_list = []
        obsDatetime_list = {}
        result_list = uuid_result.json()["results"]
        for j in range(0, len(result_list)):
            results = uuid_result.json()["results"][j]["obs"]
        #     print(results)
            for i in results:
                value = (i["groupMembers"][0]["value"])
                x = image_domain_link+value
                image_url_list.append(x)
                obsDatetime = i["groupMembers"][0]["obsDatetime"]
        #         print(obsDatetime)
                date_data = {x: obsDatetime[:19]}
                obsDatetime_list.update(date_data)
        context = {
            "success": True,
            "radiology_images": image_url_list,
            "obsDatetime_list": obsDatetime_list,
        }

        return Response(context)
    except Exception as Ex:
        context = {"success": False, "radiology_images": "No result found"}
        return Response(context)





@api_view(["GET"])
def get_image_report(request):
    try:
        url = settings.PREDICT_MODEL_URL
        parameters = request.query_params
        print("get_image_report(): parameters", parameters["image_url"])
        # print("get_image_report", request.get("image_url"))
        # image_url = request.get("image_url")
        headers = {
            "content-type": "application/json"
        }
        # img_url = "https://www.itnonline.com/sites/default/files/Chest.jpeg"
        image_url = parameters["image_url"]
        img_file = {"im_url": image_url}

        r = requests.post(
            url, 
            params=img_file, 
            headers=headers,
            verify=False
        )
        res = r.content.decode("utf-8")
        # print(res)
        json_acceptable_string = res.replace("'", '"')
        d = json.loads(json_acceptable_string)
        print("get_image_report(): d", d)
        pred = d["predictions"]["Predicted_Value"]
        conf = d["predictions"]["Confidence"]
        # print(f"Prediction is {pred} and confidence: {conf}")
        context = {"success": True, "Prediction": pred, "confidence": conf}

        return Response(context)
    except Exception as Ex:
        print(f"get_image_report(): Exception {Ex}")
        context = {"success": False, "message": f"Message"}

        return Response(context)


class GetRadiologyView(APIView):
    def get(self, request):
        parameters = request.query_params
        print("GetRadiologyView(): parameters", parameters["image_url"])
        # use your URL parameters

        url = settings.PREDICT_MODEL_URL
        # print("get_image_report", request.get("image_url"))
        # image_url = request.get("image_url")
        headers = {"content-type": "application/json"}
        # img_url = "https://www.itnonline.com/sites/default/files/Chest.jpeg"
        # parameters =
        img_file = {"im_url": parameters["image_url"]}
        r = requests.post(url, params=img_file, headers=headers, verify=False)
        res = r.content.decode("utf-8")
        # print(res)
        json_acceptable_string = res.replace("'", '"')
        d = json.loads(json_acceptable_string)
        pred = d["predictions"]["Predicted_Value"]
        conf = d["predictions"]["Confidence"]
        # print(f"Prediction is {pred} and confidence: {conf}")
        context = {"success": True, "Prediction": pred, "confidence": conf}

        return JsonResponse({"context": context})


# Patient prescription API
@api_view(["GET"])
def get_prescription(request, bahmniuid):
    # try:
    # b1e50e02-c2d1-40db-83e8-73d8d5143a0f
    # url = "https://bnopenmrs.accelx.net/openmrs/ws/rest/v1/visit?patient=" + bahmniuid
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/visit?patient=" + bahmniuid
    uuid_result = requests.get(url, auth=("superman", "Admin123"), verify=False)

    print("get_prescription(): uuid_result", uuid_result)

    all_drug_info_list = []
    scheduledDateList = []
    for links in uuid_result.json()["results"]:
        # link = (links["links"][0]["uri"])[35:]
        link = (links["links"][0]["uri"])  # by masuk
        print("link", link)

        link_uri = requests.get(link, auth=("superman", "Admin123"), verify=False)
        result_encounters = link_uri.json()["encounters"]

        for result_encounters_links in result_encounters:
            # result_encounters_links = (result_encounters_links["links"][0]["uri"])[35:]
            result_encounters_links = (result_encounters_links["links"][0]["uri"])  # by masuk
            # drug_list.append(result_encounters_links)

            encounters_links = requests.get(result_encounters_links, auth=("superman", "Admin123"), verify=False)
            drug_orders = encounters_links.json()["orders"]

            drugorder = []
            for order in drug_orders:
                if order["type"] == "drugorder":
                    drugorder.append(order)

            for drug_orders_links in drugorder:
                # drug_orders_links = (drug_orders_links["links"][0]["uri"])
                drug_orders_links = (drug_orders_links["links"][0]["uri"])  # by masuk
                # drug_list.append(drug_orders_links)

                # all_drug_info = []
                drugs = requests.get(drug_orders_links, auth=("superman", "Admin123"), verify=False)
                drug_info = drugs.json()

                # getting scheduled Date
                scheduledDate = drug_info["scheduledDate"][:10]
                if scheduledDate not in scheduledDateList:
                    scheduledDateList.append(scheduledDate)

                # drug = {'patient' : drug_info['patient']['display'], 'encounter' : drug_info['encounter']['display'], 'scheduledDate' : drug_info['scheduledDate'], 'display' : drug_info['display'], 'encounter' : drug_info['orderer']['display'], 'dose' : drug_info['dose'], 'doseUnits' : drug_info['doseUnits']['display'], 'frequency' : drug_info['frequency']['display'], 'quantity' : drug_info['quantity'], 'durationUnits' : drug_info['durationUnits']['display'], 'duration' : drug_info['duration'], 'dosingInstructions' : (drug_info['dosingInstructions'].replace("\\", ''))[1:-1]}

                hh = drug_info["dosingInstructions"]
                kk = hh.replace("\\", "")

                res = json.loads(kk)
                # drug = {'scheduledDate' : drug_info['scheduledDate'],'dosingInstructions' : res}
                encounter = drug_info["orderer"]["display"]
                remove_int_enc = re.sub("[0-9]+", "", encounter)
                encounter = remove_int_enc.replace("-", "")

                drug = {
                    "patient": drug_info["patient"]["display"],
                    "scheduledDate": drug_info["scheduledDate"],
                    "display": drug_info["display"],
                    "encounter": encounter,
                    "dose": drug_info["dose"],
                    "doseUnits": drug_info["doseUnits"]["display"],
                    "frequency": drug_info["frequency"]["display"],
                    "quantity": drug_info["quantity"],
                    "durationUnits": drug_info["durationUnits"]["display"],
                    "duration": drug_info["duration"],
                    "dosingInstructions": res,
                }

                # print(type(kk))

                all_drug_info_list.append(drug)

    # print('scheduledDateList', scheduledDateList)

    finalList = []
    for date in scheduledDateList:
        sameDatedrug = []
        for dictt in all_drug_info_list:
            if date == dictt["scheduledDate"][:10]:
                sameDatedrug.append(dictt)
        finalList.append(sameDatedrug)

    # print('finalList',finalList)

    context = {"success": True, "all_drug_info_list": finalList}

    return JsonResponse(context)

    # except Exception as Ex:
    #     # print("not ok")
    #     print(f"get_prescription(): Exception {Ex}")
    #     context = {"success": False, "result": "not-found"}

    #     return JsonResponse(context)


@api_view(["POST"])
def patientApi(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/patient/"
    payload = request.data
    headers = {"content-type": "application/json"}
    r = requests.post(url, auth=("superman", "Admin123"), data=json.dumps(payload), headers=headers, verify=False)
    return Response(r.json())


# def organization_result_view(request, org_name):
#     try:
#         context = []
#         records = getOrganization(org_name)
#         for record in records:
#             result_id = record[34]
#             print("result_id", result_id)
#             lab_result = get_lab_result_by_id(result_id)
#             # print("lab_result", lab_result)

#             # get test details
#             test_id = record[33]
#             test_details = get_test_details(test_id)
#             data = {
#                 "organization_id": record[0],
#                 "name": record[1],
#                 "city": record[2],
#                 "zip_code": record[3],
#                 "street_address": record[9],
#                 "is_active": record[16],
#                 "lab_result": {"result_id": lab_result[0], "value": lab_result[5], "test_name": test_details[3]},
#                 "referral_request_data": record[30],
#             }

#             context.append(data)
#         # print(context)
#         return JsonResponse(data={"success": True, "organizations": context}, safe=False)

#     except (Exception, psycopg2.Error) as error:
#         print("Error in update operation", error)
#         return JsonResponse(data={"success": False, "error": error})


def organization_result_view(request, org_name):
    try:
        context = []
        records = get_organization_data(org_name)
        for record in records:
            result_id = record[34]
            print("result_id", result_id)
            lab_result = get_lab_result_by_id(result_id)
            # print("lab_result", lab_result)

            # get test details
            test_id = record[33]
            # print("test_id", test_id)
            test_details = get_test_details(test_id)
            analysis_data = get_analysis_by_test_id(test_id)
            # print("organization_result_view: analysis_info", analysis_data)
            patinet_id = analysis_data[1]
            sample_id = analysis_data[0]

            patient_identity = get_patient_identity_by_patient_id(patinet_id)
            # print("organization_result_view: analysis_info", analysis_data[0])
            patient = get_patient_information_by_id(patinet_id)
            person_id = patient[1]
            person = get_person_by_id(person_id)
            sample = get_sample_by_id(sample_id)
            data = {
                "organization_id": record[0],
                "name": record[1],
                "city": record[2],
                "zip_code": record[3],
                "street_address": record[9],
                "is_active": record[16],
                "lab_result": {
                    "result_id": lab_result[0],
                    "value": lab_result[5],
                    "test_name": test_details[3],
                    "patient": {
                        "patient_id": patinet_id,
                        "patient_identifire": patient_identity[0],
                    },
                    "person": {
                        "person_id": person[0],
                        "first_name": person[1],
                        "last_name": person[2],
                        "middle_name": person[3],
                    },
                    "sample": {
                        "sample_id": sample[0],
                        "accession_number": sample[1],
                        "entered_date": sample[6],
                    },
                },
                "referral_request_data": record[30],
            }

            context.append(data)
        # print(context)
        # return context
        # print(context)
        return JsonResponse(data={"success": True, "organizations": context}, safe=False)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
        return JsonResponse(data={"success": False, "error": error})


# @api_view(["POST"])
# def result_update_view(request):
#     try:
#         payload = request.data
#         print("result_update_view: payload", payload["result_id"])
#         value = payload["value"]
#         result_id = payload["result_id"]
#         record = update_result(result_id, value)

#         # print(context)
#         return JsonResponse(data={"success": True, "result": record}, safe=False)

#     except (Exception, psycopg2.Error) as error:
#         print("Error in update operation", error)
#         return JsonResponse(data={"success": False, "error": error})


def result_update_view(request, result_id, value):
    try:
        # payload = request.data
        # print("result_update_view: payload", payload["result_id"])
        # value = payload["value"]
        # result_id = payload["result_id"]
        record = update_result(result_id, value)

        # print(context)
        return JsonResponse(data={"success": True, "result": record}, safe=False)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
        return JsonResponse(data={"success": False, "error": error})


@api_view(["POST"])
def find_appointment_schedule_doctor(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService/all/full"
    headers = {"content-type": "application/json"}
    all_services_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)

    def find_day(date):
        date = str(date)
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        return day_name[day]

    def time_sceduler(minutes, my_find_scedule_start, my_find_scedule_endtime, date):
        curr_time = datetime.datetime.strptime(my_find_scedule_start, '%H:%M:%S')
        end_time = datetime.datetime.strptime(my_find_scedule_endtime, '%H:%M:%S')
        seq1 = []
        # getting all appointment list using services uid
        appointment_list = Appointment.objects.all().filter(serviceUuid=services_name, status=True)
        ## getting serializer data
        existing_appointment = AppointmentSerializer(appointment_list, many=True)
        existing_appointment_date_time_list = []

        for ex_appointment in existing_appointment.data:
            # print("ex_appointment",ex_appointment['startDateTime'])
            existing_appointment_date_time_list.append(ex_appointment['startDateTime'])
        print(existing_appointment_date_time_list)
        
        counter = 0
        while curr_time < end_time:
            if counter == 0:
                # seq1.append({f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
                c_date_time = f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z'
                if c_date_time not in existing_appointment_date_time_list:
                    seq1.append({f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
                    
            else:
                curr_time = curr_time + timedelta(minutes=minutes)
                c_date_time = f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z'
                print('c_date_time', c_date_time)
                if c_date_time in existing_appointment_date_time_list:
                    print('true')
                else:
                    seq1.append({f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
            counter += 1
        return seq1

    my_find_services = []
    #providing services uid and date we will get schedule list
    def find_services(services_name, date):
        my_find_scedule_startime = ''
        my_find_scedule_endtime = ''
        for service in all_services_response.json():
            if service['uuid'] == services_name:
                my_find_services.append(service)
                day = (find_day(date)).lower()
                # print(day)
                # durationMins = int(service['durationMins'])
                print('durationMins', service['durationMins'])
                print('startTime', service['startTime'])
                my_find_scedule_startime = (service['startTime'])
                my_find_scedule_endtime = (service['endTime'])
                for weekly_services in service['weeklyAvailability']:
                    # print((weekly_services['dayOfWeek']).lower())
                    ser_day = ((weekly_services['dayOfWeek']).lower())
                    if ser_day == day:
                        my_find_scedule_startime = (weekly_services['startTime'])
                        my_find_scedule_endtime = (weekly_services['endTime'])
        result = time_sceduler(int(service['durationMins']), my_find_scedule_startime, my_find_scedule_endtime, date)
        return result

    services_name = request.data['services_name']
    date = request.data['date']
    final_result = find_services(services_name, date)

    return Response(final_result)


@api_view(["POST"])
def find_appointment_schedule_assistant(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService/all/full"
    headers = {"content-type": "application/json"}
    all_services_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)

    def find_day(date):
        date = str(date)
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        return day_name[day]

    def time_sceduler(minutes, my_find_scedule_start, my_find_scedule_endtime, date):
        curr_time = datetime.datetime.strptime(my_find_scedule_start, '%H:%M:%S')
        end_time = datetime.datetime.strptime(my_find_scedule_endtime, '%H:%M:%S')
        seq1 = []
        # getting all appointment list using services uid
        appointment_list = Appointment.objects.all().filter(assistant_serviceUuid=services_name, status=True)

        ## getting serializer data
        existing_appointment = AppointmentSerializer(appointment_list, many=True)
        existing_appointment_date_time_list = []
        print('appointment_list', existing_appointment.data)

        for ex_appointment in existing_appointment.data:
            # print("ex_appointment",ex_appointment['startDateTime'])
            existing_appointment_date_time_list.append(ex_appointment['startDateTime'])
        print(existing_appointment_date_time_list)
        counter = 0
        while curr_time < end_time:
            if counter == 0:
                # seq1.append({f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
                c_date_time = f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z'
                if c_date_time not in existing_appointment_date_time_list:
                    seq1.append({f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
            else:
                curr_time = curr_time + timedelta(minutes=minutes)
                c_date_time = f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z'
                # print(c_date_time)
                if c_date_time in existing_appointment_date_time_list:
                    print('true')
                else:
                    seq1.append({f'{date}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
            counter += 1
        return seq1

    my_find_services = []
    #providing services uid and date we will get schedule list
    def find_services(services_name, date):
        my_find_scedule_startime = ''
        my_find_scedule_endtime = ''
        for service in all_services_response.json():
            print('service', service)
            if service['uuid'] == services_name:
                my_find_services.append(service)
                day = (find_day(date)).lower()
                # print(day)
                # durationMins = int(service['durationMins'])
                # print(durationMins)
                my_find_scedule_startime = (service['startTime'])
                my_find_scedule_endtime = (service['endTime'])
                for weekly_services in service['weeklyAvailability']:
                    # print((weekly_services['dayOfWeek']).lower())
                    ser_day = ((weekly_services['dayOfWeek']).lower())
                    if ser_day == day:
                        my_find_scedule_startime = (weekly_services['startTime'])
                        my_find_scedule_endtime = (weekly_services['endTime'])
        result = time_sceduler(int(service['durationMins']), my_find_scedule_startime, my_find_scedule_endtime, date)
        return result

    services_name = request.data['services_name']
    date = request.data['date']
    final_result = find_services(services_name, date)

    return Response(final_result)


# Get all services
@api_view(["GET"])
def get_all_services(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService/all/full"
    headers = {"content-type": "application/json"}
    all_services_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)
    # location_list = []
    service_list = []
    for service in all_services_response.json():
        # location_list.append({service['location']['name']: service['location']['uuid']})
        service_list.append({service['name']: service['uuid']})
    result = {'service_list': service_list}
    return Response(result)


# Get all provider
@api_view(["GET"])
def get_all_provider(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/provider"
    headers = {"content-type": "application/json"}
    all_provider_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)
    provider_list = []
    for provider in all_provider_response.json()['results']:
        provider_list.append({provider['display']: provider['uuid']})
    return Response(provider_list)


@api_view(["POST"])
def edn_time(request):
    services_name = request.data['services_name']
    date = request.data['date']
    day = request.data['day']
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService/all/full"
    headers = {"content-type": "application/json"}
    all_services_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)

    def ending_time_sceduler(minutes, my_find_scedule_start, day):
        # day_date = datetime.datetime.strptime(day, '%Y-%m-%d')
        in_time = datetime.datetime.strptime(my_find_scedule_start, "%I:%M %p")
        my_find_scedule_start = datetime.datetime.strftime(in_time, "%H:%M:%S")
        print(my_find_scedule_start)

        curr_time = datetime.datetime.strptime(my_find_scedule_start, '%H:%M:%S')
        seq1 = []
        curr_time = curr_time + timedelta(minutes=minutes)
        seq1.append({f'{day}T{curr_time.strftime("%H:%M:%S")}.000Z': curr_time.strftime("%I:%M %p")})
        return seq1

    def find_services(services_name, given_time):
        result = []
        for service in all_services_response.json():
            print(service['name'])
            print(services_name)
            if service['uuid'] == services_name:
                result = ending_time_sceduler(int(service['durationMins']), given_time, day)
            else:
                continue
        return result

    results = find_services(services_name, date)
    print('my_find_services result', results)
    return Response(results)


@api_view(["POST"])
def create_appointment(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointments"
    appointment_data = request.data
    headers = {"content-type": "application/json"}
    r = requests.post(url, auth=("superman", "Admin123"), data=json.dumps(appointment_data), headers=headers,
                      verify=False)
    return Response(r.json())


@api_view(["GET"])
def get_all_doctors(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService/all/full"
    headers = {"content-type": "application/json"}
    all_services_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)
    doctor_list = []

    for service in all_services_response.json():
        provider_uid = (service['name'].split("+"))[1]
        provider_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/provider/" + provider_uid
        headers = {"content-type": "application/json"}
        specific_doctor = requests.get(provider_url, auth=("superman", "Admin123"), headers=headers, verify=False)
        # print(specific_doctor.json())
        if specific_doctor.json()['identifier'] == 'doctor':
            persion_uuid = specific_doctor.json()['person']['uuid']
            persion_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/person/" + persion_uuid
            headers = {"content-type": "application/json"}
            persion_response = requests.get(persion_url, auth=("superman", "Admin123"), headers=headers, verify=False)
            doctor_dict = {
                "doctor_name": persion_response.json()['display'],
                'speciality': service['speciality']['name'],
                'gender': persion_response.json()['gender'], 'location': service['location']['name'],
                'maxAppointmentsLimit': service['maxAppointmentsLimit'], 'service_uuid': service['uuid'],
                'doctor_uuid': specific_doctor.json()['uuid']
            }
            doctor_list.append(doctor_dict)
    return Response(doctor_list)


@api_view(["GET"])
def get_all_assistant(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService/all/full"
    headers = {"content-type": "application/json"}
    all_services_response = requests.get(url, auth=("superman", "Admin123"), headers=headers, verify=False)
    assistant_list = []

    for service in all_services_response.json():
        provider_uid = (service['name'].split("+"))[1]
        provider_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/provider/" + provider_uid
        headers = {"content-type": "application/json"}
        specific_assistant = requests.get(provider_url, auth=("superman", "Admin123"), headers=headers, verify=False)
        print(specific_assistant.json())
        if specific_assistant.json()['identifier'] == 'assistant':
            persion_uuid = specific_assistant.json()['person']['uuid']
            persion_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/person/" + persion_uuid
            headers = {"content-type": "application/json"}
            persion_response = requests.get(persion_url, auth=("superman", "Admin123"), headers=headers, verify=False)
            assistant_dict = {
                "doctor_name": persion_response.json()['display'],
                'gender': persion_response.json()['gender'],
                'location': service['location']['name'],
                'maxAppointmentsLimit': service['maxAppointmentsLimit'],
                'service_uuid': service['uuid'],
                'assitent_uuid': specific_assistant.json()['uuid']
            }
            assistant_list.append(assistant_dict)
    return Response(assistant_list)


def get_prescription_api(**args):
    """
    get prescription information using patient uuid
    """
    try:
        patient_uuid = args['patient_uuid']
        presvription_url = f"{settings.BAHMNI_API_BASE_URL}/openmrs/ws/rest/v1/bahmnicore/drugOrders/prescribedAndActive?getEffectiveOrdersOnly=false&getOtherActive=true&numberOfVisits=10&patientUuid={patient_uuid}&preferredLocale=en"

        response = requests.get(presvription_url, auth=("superman", "Admin123"), verify=False)

        #         print(f"get_prescription_api {response.json}")

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'get_prescription_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'get_prescription_api(): Other error occurred: {err}')
    else:
        print('get_prescription_api(): Success!')

    return response



def get_radiology_order(**args):
    """
    get all radiology order by patient uuid and visiting uuid
    """
    try:
        patient_uuid = args['patient_uuid']
        visit_uuid = args['visit_uuid']
        presvription_url = f"{settings.BAHMNI_API_BASE_URL}/openmrs/ws/rest/v1/bahmnicore/orders?includeObs=true&orderTypeUuid=8189dbdd-3f10-11e4-adec-0800271c1b75&patientUuid={patient_uuid}&visitUuid={visit_uuid}"

        response = requests.get(presvription_url, auth=("superman", "Admin123"), verify=False)
        
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'get_radiology_order(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'get_radiology_order(): Other error occurred: {err}')
    else:
        print('get_radiology_order(): Success!')

    return response


def get_lab_orders_api(**args):
    """
    get lab order information using patient uuid
    """
    try:
        patient_uuid = args['patient_uuid']
        presvription_url = f"{settings.BAHMNI_API_BASE_URL}/openmrs/ws/rest/v1/bahmnicore/labOrderResults?numberOfVisits=10&patientUuid={patient_uuid}"
        
        response = requests.get(presvription_url, auth=("superman", "Admin123"), verify=False)
        
#         print(f"get_prescription_api {response.json}")

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'get_lab_orders_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'get_lab_orders_api(): Other error occurred: {err}')
    else:
        print('get_lab_orders_api(): Success!')


    return response


@api_view(["GET"])
def get_patient_visit_list(request, patient_uuid):
    response = get_prescription_api(patient_uuid=patient_uuid)
    visitDrugOrders = response.json()["visitDrugOrders"]
    visitDrugOrderVisitUuidList = []

    uuidList = []

    for visitDrugOrder in visitDrugOrders:
        #         print(visitDrugOrder["visit"]["uuid"])

        if visitDrugOrder["visit"]["uuid"] not in uuidList:
            data = {
                "visitUuid": visitDrugOrder["visit"]["uuid"],
                "startDateTime": visitDrugOrder["visit"]["startDateTime"]
            }
            uuidList.append(visitDrugOrder["visit"]["uuid"])
            visitDrugOrderVisitUuidList.append(data)
    #     print(visitDrugOrderVisitUuidList)

    # return visitDrugOrderVisitUuidList
    return Response(visitDrugOrderVisitUuidList)


@api_view(["GET"])
def get_visit_medication_details(request, patient_uuid, visit_uuid):
    response = get_prescription_api(patient_uuid=patient_uuid)
    visitDrugOrders = response.json()["visitDrugOrders"]

    lab_order_response = get_lab_orders_api(patient_uuid=patient_uuid)
    single_drug_visit = visitDrugOrders[0]
    visitLabOrders = lab_order_response.json()["results"]
    visit_time = single_drug_visit["visit"]['startDateTime']
    print(visit_time)

    radiology_order_response = get_radiology_order(patient_uuid=patient_uuid,visit_uuid=visit_uuid)

    drugOrderDataList = []
    labOrderList = []
    radiologyOrderList = []
    for visitDrugOrder in visitDrugOrders:
        if visitDrugOrder["visit"]["uuid"] == visit_uuid:
            drugOrderDataList.append(visitDrugOrder)
    for visitLabOrder in visitLabOrders:
        if visitLabOrder["visitStartTime"] == visit_time:
            labOrderList.append(visitLabOrder)
    for radiology_order in radiology_order_response.json():
        radiologyOrderList.append(radiology_order)

    # context ={
    #     'drugOrderDataList':drugOrderDataList,
    #     'labOrderList': labOrderList,
    #     'radiologyOrderList': radiologyOrderList
    # }
    context ={
        'drugOrderDataList':drugOrderDataList,
        'labAndRadiologyOrderList': {'labOrderList':labOrderList,'radiologyOrderList':radiologyOrderList}
    }
    return Response(context)


@api_view(["GET"])
def cancle_appointment(request, bahmni_appointment_id):
    try:
        status_change_url =  f"{settings.BAHMNI_API_BASE_URL}/openmrs/ws/rest/v1/appointments/{bahmni_appointment_id}/status-change"

        payload = {"toStatus": "Cancelled",
                   "applyForAll": "false",
                   "timeZone": "Asia/Dhaka"}
        headers = {"Content-Type": "application/json"}
        response = requests.post(status_change_url, auth=("superman", "Admin123"),data=json.dumps(payload),headers=headers, verify = False)

        context = {
            "status": True,
            "data": response.json()
        }

        return Response(context)

    except Exception as Ex:
        context = {
            "status": False,
        }

        return Response(context)



@api_view(["POST"])
def opd_visit_on(request):
    url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/visit"
    appointment_data = request.data
    headers = {"content-type": "application/json"}
    r = requests.post(url, auth=("superman", "Admin123"), data=json.dumps(appointment_data), headers=headers,
                      verify=False)
    return Response(r.json())


class HelpListApiView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Help.objects.all()
    serializer_class = HelpSerialiser

    def get(self, request):
        return self.list(request)


#get location from bhamni
@api_view(["GET"])
def get_all_location_bhamni(request):
    try:
        location_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/location?operator=ALL&s=byTags&tags=Appointment+Location&v=default"
        response = requests.get(location_url, auth=("superman", "Admin123"),verify=False)
        # return Response(response.json())
        context = {
            "status": True,
            "data": response.json()['results']
        }
        return Response(context)
    except Exception as Ex:
        context = {
            "status": False,
        }
        return Response(context)


#get speciality from bhamni
@api_view(["GET"])
def get_all_speciality_bhamni(request):
    try:
        speciality_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/speciality/all"
        response = requests.get(speciality_url, auth=("superman", "Admin123"),verify=False)
        # return Response(response.json())
        context = {
            "status": True,
            "data": response.json()
        }
        return Response(context)
    except Exception as Ex:
        context = {
            "status": False,
        }
        return Response(context)


#creating services in bhamni
@api_view(["POST"])
def create_service_bhamni(request):
    try:
        create_service_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService"
        payload = request.data
        print("payload", payload)
        headers = {"content-type": "application/json"}
        r = requests.post(create_service_url, auth=("superman", "Admin123"), data=json.dumps(payload), headers=headers, verify=False)
        
        context ={
            "status": True,
            "data": r.json()
        }
        return Response(context)
    except:
        context ={
            "status": False
        }
        return Response(context)

@api_view(["POST"])
def update_service_bhamni(request):
    try:
        update_service_url = settings.BAHMNI_API_BASE_URL + "/openmrs/ws/rest/v1/appointmentService"
        payload = request.data
        print("payload", payload)
        headers = {"content-type": "application/json"}
        r = requests.post(update_service_url, auth=("superman", "Admin123"), data=json.dumps(payload), headers=headers, verify=False)
        
        context ={
            "status": True,
            "data": r.json()
        }
        return Response(context)
    except:
        context ={
            "status": False
        }
        return Response(context)
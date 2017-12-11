#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
from __future__ import absolute_import
from __future__ import unicode_literals
from apps.fhir.bluebutton.models import Crosswalk
from apps.fhir.bluebutton.utils import get_resourcerouter
from django.conf import settings

__author__ = "Alan Viars"


def set_sample_patient_id(backend, user, response, *args, **kwargs):
    """If authenticating through Google, set patient_id to sample."""

    if backend.name == 'google-oauth2':
        fhir_source = get_resourcerouter()
        cx, g_o_c = Crosswalk.objects.get_or_create(
            user=user, fhir_source=fhir_source)
        cx.fhir_id = getattr(settings, 'DEFAULT_SAMPLE_FHIR_ID', '3979')
        cx.save()
        return {'fhir_id': cx.fhir_id, 'patient_id': cx.fhir_id}
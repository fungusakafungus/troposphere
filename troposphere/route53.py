# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty
from .validators import integer


class AliasTarget(AWSHelperFn):
    def __init__(self, hostedzoneid, dnsname):
        self.data = {
            'HostedZoneId': hostedzoneid,
            'DNSName': dnsname,
        }

    def JSONrepr(self):
        return self.data


class RecordSet(AWSProperty):
    # This is for use in a list with RecordSetGroup (below)
#    dictname = 'Properties'
    props = {
        'AliasTarget': (AliasTarget, False),
        'Comment': (basestring, False),
        'HostedZoneId': (basestring, False),
        'HostedZoneName': (basestring, False),
        'Name': (basestring, True),
        'Region': (basestring, False),
        'ResourceRecords': (list, False),
        'SetIdentifier': (basestring, False),
        'TTL': (integer, False),
        'Type': (basestring, True),
        'Weight': (integer, False),
    }


class RecordSetType(RecordSet, AWSObject):
    # This is a top-level resource
    type = "AWS::Route53::RecordSet"


class RecordSetGroup(AWSObject):
    type = "AWS::Route53::RecordSetGroup"

    props = {
        'HostedZoneId': (basestring, False),
        'HostedZoneName': (basestring, False),
        'RecordSets': (list, False),
        'Comment': (basestring, False),
    }

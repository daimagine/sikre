# Copyright 2014-2015 Clione Software and Havas Worldwide London
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import binascii
import os

import peewee as orm

from sikre.db.connector import ConnectionModel
from sikre.models.users import User
from sikre.models.items import Category, Item
from sikre.models.services import Service


RESOURCE = (
    (0, "Category"),
    (1, "Item"),
    (2, "Service"),
)

USED = (
    (0, "No"),
    (1, "Yes"),
)


class ShareToken(ConnectionModel):

    """
    Standard user model. Stores minimal data about the user to handle the
    authentication, like email, username, and auth token, apart from some
    extra parameters for administration.
    """
    user = orm.ForeignKeyField(User)
    token = orm.CharField(unique=True, null=True)
    resource = orm.IntegerField(choices=RESOURCE, null=True)
    resource_id = orm.IntegerField(null=True)
    email = orm.CharField(null=True)
    used = orm.IntegerField(choices=USED, null=True)

    def is_valid(self):
        if self.used:
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        return super(ShareToken, self).save(*args, **kwargs)

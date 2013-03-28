#
# Copyright (c) 2013 Murph Finnicum.
#
# Permission is granted to use this code for any purpose except that
# you may not use any portion of it as part of a MP2 submission for
# CS498stk at UIUC.
#
# This code is provided by the author 'as is' and comes without any
# warranty (Express, limited, or otherwise). In no event shall the
# author be liable for any damages or liability arising from the use
# of this code.
#


import logging
import os

from google.appengine.ext import ndb

class Participant(ndb.Model):
    user = ndb.StringProperty(indexed=False)
    cash = ndb.IntegerProperty(indexed=False)
    hasCredit = ndb.BooleanProperty(indexed=False)
    wantsToPayForEverything = ndb.IntegerProperty(indexed=False)
    costOfMeal = ndb.IntegerProperty(indexed=False)
    
    result = ndb.StringProperty(indexed=False)
    

class Table(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    users = ndb.LocalStructuredProperty(Participant, repeated=True)

    # After everything goes down, it's resolved
    hasResolved = ndb.BooleanProperty(default=False, indexed=True)

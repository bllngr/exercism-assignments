#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import calendar

# Submission file for the python meetup_test exercise.
#
# v1: 

cal = calendar.Calendar()

def ordinal(index):
	ords = ['1st', '2nd', '3rd', '4th', 'last']
	return ords[index]

def meetup_day(day):
	"""
	Given a date, return the date of meetups which usually happen every
	month on the same day of the week (in the Gregorian calendar).

	Example: 2013-05-07 is the first Tuesday of May 2013, so the
	function returns (2013, 5, 'Tuesday', '1st').
	"""
	# day of the week as an integer, where Monday is 0 and Sunday is 6
	weekday = day.weekday()

	weekday_str = day.strftime('%A')
	
	# list of (day_number, weekday_number) tuples
	weekdays = cal.itermonthdays2(day.year, day.month)

	# list of the same weekdays in the given month
	same_weekdays = [day for day in weekdays if day[2] == weekday]

	# index of the given weekday
	weekday_index = [x[0] for x in same_weekdays].index(day.day)

	return ordinal(weekday_index)


	# finde heraus, welcher Tag im Monat der weekday ist
	# 1st, 2nd, 3rd, 4th, and last


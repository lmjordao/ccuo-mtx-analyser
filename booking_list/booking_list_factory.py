"""

"""
from booking_list.ip_booking_list import IPBookingList


class BookingListFactory:

    @staticmethod
    def create(book_info):
        if book_info['type'] == 'ip':
            return IPBookingList(book_info)

        # TODO: add remaining types

import re
from wsgiref.util import request_uri
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from pages import models

# Create your views here.


def display_messages(request):
    data = models.Messages.objects.all()
    context = {"table": data}
    return render(request, "home.html", context)


def covert_channel(request):
    if request.method == "GET":
        if request.path != "/" or request.path != "/results/":

            # parse and decode message
            hex_values = []
            byte_rcnstrctd = []
            hex_bytes = []
            msg_rcnstrctd = []
            ascii_str = []
            res_path = str(request.path)
            res_parts = res_path.split(".")[0]  # removing file enxtension
            hex_words = res_parts.split("/")[1:]  # stripping empty first string
            for hex_string in hex_words:
                hex_byte_space = re.split("-|_|!|&|%", hex_string)[
                    :2
                ]  # Splitting two hex values apart whitespace to give byte representation
                print(hex_byte_space)
                for single_byte in hex_byte_space:
                    hex_values.append(len(single_byte) - 1)
            for i in range(
                0, len(hex_values) - 1, 2
            ):  # loop converts strings to hex and concatenates values
                value_to_hex1 = hex(hex_values[i]).split("x")[1]
                value_to_hex2 = hex(hex_values[i + 1]).split("x")[1]
                byte_rcnstrctd.append(str(value_to_hex1) + str(value_to_hex2))
            for (
                byte
            ) in byte_rcnstrctd:  # loop appends 0x notation for hex conversion later
                hex_bytes.append("0x" + byte)
            for hex_byte in hex_bytes:  # loop converts hex back to ASCII
                msg_rcnstrctd = bytes.fromhex(hex_byte[2:])
                ascii_str.append(msg_rcnstrctd.decode())
            ascii_str = "".join(ascii_str)
            # add message to database
            new_row = models.Messages(uri=res_path, message=ascii_str)
            new_row.save()
    return render(request, "home.html")

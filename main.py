from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential
import json

client = FormRecognizerClient("https://hedefreader.cognitiveservices.azure.com/", AzureKeyCredential("602efdabf61747a0aedbb70d5c503ba8"))

receiptUrl = "https://raw.githubusercontent.com/kaptanmajere/receipt-samples/main/Screenshot_1.png"
receipt_recognizer = client.begin_recognize_receipts_from_url(receiptUrl)

result = receipt_recognizer.result()
for receipt in result:
    for name, field in receipt.fields.items():
        if name == "Items":
            print("Receipt Items:")
            for idx, items in enumerate(field.value):
                print("...Item #{}".format(idx + 1))
                for item_name, item in items.value.items():
                    print("......{}: {} has confidence {}".format(item_name, item.value, item.confidence))
        else:
            print("{}: {} has confidence {}".format(name, field.value, field.confidence))

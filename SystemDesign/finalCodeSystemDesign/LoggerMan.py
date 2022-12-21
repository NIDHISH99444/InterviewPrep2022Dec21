# class Logger:
#
#     def __init__(self,next_entry,count):
#         self.next_entry=next_entry
#         self.count=count
#
#     def make_entry(self,message):
#         pass
#
#     def log(self,message):
#         self.make_entry(message)
#         if self.next_entry is None:
#             return
#         else:
#             self.next_entry.log(message)
#
#
# class InfoLogger(Logger):
#     def make_entry(self, message):
#         print("Info", message)
#
#
# class ErrorLogger(Logger):
#     def make_entry(self,message):
#         print("Error",message)

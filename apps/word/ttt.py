from apps.account import models

print(models.User._meta.app_label, '<--')
print(models.User._meta.model_name, '<<<<')

from django.urls import path

from contacts.api.views import AllContacts, ContactsEditDelete

urlpatterns = [
    path('list-create-contacts/', AllContacts.as_view(), name='list-edit-contacts'),
    path('edit-delete-contacts/<int:pk>/', ContactsEditDelete.as_view(), name='edit-delete-contacts'),
]
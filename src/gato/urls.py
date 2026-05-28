from django.urls import path

from gato.views import (
    CategoriaCreate,
    CategoriaDelete,
    CategoriaDetail,
    CategoriaList,
    CategoriaUpdate,
    GatoCreate,
    GatoDelete,
    GatoDetail,
    GatoList,
    GatoUpdate,
    SolicitudAdopcionCreate,
    SolicitudAdopcionDelete,
    SolicitudAdopcionDetail,
    SolicitudAdopcionList,
    SolicitudAdopcionUpdate,
)

app_name = "gato"

urlpatterns = [                                      
    path("categoria/", CategoriaList.as_view(), name="categoria_home"

    ),
    path("categoria/create/", CategoriaCreate.as_view(), name="categoria_create"
    
    ),
    path(
        "categoria/update/<int:pk>", CategoriaUpdate.as_view(), name="categoria_update"
    ),
    path(
        "categoria/detail/<int:pk>", CategoriaDetail.as_view(), name="categoria_detail"
    ),
    path(
        "categoria/delete/<int:pk>", CategoriaDelete.as_view(), name="categoria_delete"
    ),
    path("gato/", GatoList.as_view(), name="gato_home"

    ),
    path("gato/create/", GatoCreate.as_view(), name="gato_create"
    
    ),
    path("gato/update/<int:pk>", GatoUpdate.as_view(), name="gato_update"
         
    ),
    path("gato/detail/<int:pk>", GatoDetail.as_view(), name="gato_detail"
          
    ),
    path("gato/delete/<int:pk>", GatoDelete.as_view(), name="gato_delete"
         
    ),
    path("solicitud/", SolicitudAdopcionList.as_view(), name="solicitud_home"
    
    ),
    path("solicitud/create/", SolicitudAdopcionCreate.as_view(), name="solicitud_create"
 
    ),
    path("solicitud/update/<int:pk>", SolicitudAdopcionUpdate.as_view(), name="solicitud_update"
    
    ),
    path("solicitud/detail/<int:pk>", SolicitudAdopcionDetail.as_view(), name="solicitud_detail"
    
    ),
    path("solicitud/delete/<int:pk>", SolicitudAdopcionDelete.as_view(), name="solicitud_delete"
    
    ),
]


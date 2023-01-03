from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


#? herkes okusun ama sadece admin olan create/update yapabilmesi için ilave bir metod yazdık.
#? aslında BasePermission içinde olan IsAuthenticatedOrReadOnly metodunu override ettik

""" override edilen metod;
class IsAuthenticatedOrReadOnly(BasePermission):
    ""
    The request is authenticated as a user, or is a read-only request.
    ""

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
"""

#? 1nci yöntem; biz yazdık (yapay zeka)
class IsAdminUserOrReadOnly(BasePermission):  #? IsAdminUserOrReadOnly bu ismi  biz yazdık
  """ 
  Buraya metod için açıklayıcı bir docstring yazılabilir.
  Herkes okusun ama sadece admin olan create/update yapabilsin  
  """
  def has_permission(self, request, view):
    if request.method in ['GET']:
      return True
    else:
      return request.user.is_staff



#? 2nci yöntem; sinan hoca yazdı
class IsAdminOrReadOnly(BasePermission):
    # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

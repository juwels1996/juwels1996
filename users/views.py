from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, UserMemories  # Adjust if using a custom user model
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()  # Fetch all user objects
    serializer_class = UserSerializer

@api_view(['GET'])
def index(request):

    #users = CustomUser.objects.all().values("id", "username","profile_image","ssc_batch","address")
    users = CustomUser.objects.all()
    context = {}
    user_data_list = []
    for user in users:
        user_dict = {}
        user_dict['id'] = user.id
        user_dict['ssc_batch'] = user.ssc_batch
        user_dict['username'] = user.username
        user_dict['phone_number'] = user.phone_number
        user_dict['designation'] = user.designation
        user_dict['profile_image'] = user.profile_image
        user_dict['address'] = user.address

        user_memories = UserMemories.objects.filter(user=user)
        user_dict['memories'] = list(user_memories.values())

        user_data_list.append(user_dict)

    context['user_data'] = user_data_list
    context['comment_list'] = [
        {
            'id' : 1,
            'comment' : "cc"
        },
        {
            'id' : 2,
            'comment' : "bb"
        }
    ]
    return Response(context)
    # return Response(users)


@api_view(['PATCH'])
def update_user(request,user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"error":"User Not found"},status=status.HTTP_404_NOT_FOUND)
    
    user.username = request.data.get('username', user.username)
    user.phone_number = request.data.get('phone_number',user.phone_number)
    user.designation = request.data.get('designation',user.designation)
    user.ssc_batch = request.data.get('ssc_batch',user.ssc_batch)
    user.address = request.data.get('address', user.address)
    user.profile_image = request.data.get('profile_image', user.profile_image)

    user.save()

    return Response({
        "id": user.id,
        "username":user.username,
        "phone_number": user.phone_number,
        "designation": user.designation,
        "ssc_batch":user.ssc_batch,
        "address": user.address,
        "profile_image":user.profile_image
    },
    status=status.HTTP_200_OK
    )
    


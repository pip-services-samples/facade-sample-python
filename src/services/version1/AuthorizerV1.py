# # -*- coding: utf-8 -*-

# from pip_services3_commons.errors import UnauthorizedException
# from pip_services3_rpc.auth.BasicAuthManager import BasicAuthManager
# from pip_services3_rpc.auth.RoleAuthManager import RoleAuthManager
# from pip_services3_rpc.services import HttpResponseSender

# # TODO need add
# class AuthorizerV1:
#     basic_auth = BasicAuthManager()
#     role_auth = RoleAuthManager()

#     # Anybody who entered the system
#     def anybody(self):
#         return self.basic_auth.anybody()

#     # Only registered and authenticated users
#     def signed(self):
#         return self.role_auth.user_in_role('admin')

#     # Only the user session owner
#     def owner(self, req, res, id_param='user_id', ):
#         user = req.params.get('user')
#         party_id = req.params.get(id_param)
#         if user is None:
#             HttpResponseSender.send_error(
#                 UnauthorizedException(
#                     None, 'NOT_SIGNED',
#                     'User must be signed in to perform this operation'
#                 ).with_status(401)
#             )
#         elif party_id is None:
#             HttpResponseSender.send_error(
#                 UnauthorizedException(
#                     None, 'NO_USER_ID',
#                     'User id is not defined'
#                 ).with_status(401)
#             )
#         else:
#             is_owner = party_id == user['id']

#             if not is_owner:
#                 HttpResponseSender.send_error(
#                     UnauthorizedException(
#                         None, 'NOT_OWNER', 'Only user owner access is allowed'
#                     ).with_details('user_id', party_id).with_status(403)
#                 )
#             else:
#                 pass
#                 # next()

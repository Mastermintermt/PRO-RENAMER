from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("PyʀᴏBᴏᴛᴢ")

async def web_server():
    web_app = web.Application(client_max_size=50000000)  # Updated to 50 MB
    web_app.add_routes(routes)
    return web_app

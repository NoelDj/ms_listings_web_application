const privateRotues = ["/home"]
export function onRequest ({ locals, request }, next) {
  
    locals.title = "New title";
    const url = new URL(request.url);
    const pathname = url.pathname;
    if (!privateRotues.includes(pathname)){
        return next()
    }

    return Response.redirect(new URL("/login", request.url));
}
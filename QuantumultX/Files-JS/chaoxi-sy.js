var modifiedHeaders = $request.headers;

modifiedHeaders['Cookies'] = 'tide_sid=9486b41b6f814d2556b2e3b55a9a8738';

var modifiedPath = '/api2/abc?k=v';

$done({path: modifiedPath, headers : modifiedHeaders});

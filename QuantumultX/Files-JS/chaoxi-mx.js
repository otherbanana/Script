var modifiedHeaders = $request.headers;

modifiedHeaders['Cookie'] = 'tide_sid=9486b41b6f814d2556b2e3b55a9a8738';

var modifiedPath = '/v1/meditation/albums/*/resources/*/download_url';

$done({path: modifiedPath, headers : modifiedHeaders});

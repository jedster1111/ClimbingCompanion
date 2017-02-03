angular.module('logbookApp.services', []).factory('Climb', function ($resource) {
    return $resource('http://127.0.0.1:8000/logbook/climbs/:id', {
        update: {
            method: 'PUT'
        }
    });
});
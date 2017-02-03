var app = angular.module('logbookApp', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller('climbReader', function ($scope, $http) {
    $http.get('http://127.0.0.1:8000/logbook/climbs/')
        .then(function (response) {
            $scope.climbs = response;
        });
});
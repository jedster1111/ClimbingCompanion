var app = angular.module('logbookApp', ['ngAnimate']);

app.config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});


app.controller('logbookCtrl', function ($scope, $http, $timeout) {
    $scope.climbs = {};
    $scope.newClimb = {};

    $http.get('http://127.0.0.1:8000/logbook/centres/')
       .then(function (response) {
           $scope.centres = response.data;
       });
    $scope.saveNewClimb = function () {
        $http.post('/logbook/climbs/', $scope.newClimb)
        .then(function (data) {
            $http.get('http://127.0.0.1:8000/logbook/climbs/?centre=' + $scope.centre.id)
            .then(function (response) {
                $scope.climbs = response.data;
            });
        })
        .catch(function (data) {
            console.log(data);
        });
    };
       
    $scope.pickCentre = function (selected) {
        $scope.centre = selected;
        $scope.selectedClimbs = selected.climbs;
        $http.get('http://127.0.0.1:8000/logbook/climbs/?centre=' + $scope.centre.id)
            .then(function (response) {
                $scope.climbs = response.data;
                $scope.newClimb.centre = $scope.centre.id;
            });
    };
    
});

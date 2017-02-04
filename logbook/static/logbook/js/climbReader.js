var app = angular.module('logbookApp', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller('logbookCtrl', function ($scope, $http) {
    $http.get('http://127.0.0.1:8000/logbook/climbs/')
        .then(function (response) {
            $scope.climbs = response.data;
        });
    $http.get('http://127.0.0.1:8000/logbook/centres/')
       .then(function (response) {
           $scope.centres = response.data;
       });
    $scope.pickCentre = function (selected) {
        $scope.centre = selected;
        $scope.selectedClimbs = selected.climbs;
    };
});

app.filter('climbFilter', function ($filter) {
    return function (list, arrayFilter, element) {
        if (arrayFilter) {
            return $filter("filter")(list, function(listItem) {
                return arrayFilter.indexOf(listItem[element]) != -1;
            });
        }
    };
});

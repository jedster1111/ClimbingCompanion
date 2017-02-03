angular.module('logbookApp', []).controller('ClimbListController', function ($scope, $state, $window, Climb) {
    $scope.climbs = Climb.query();
}).controller('ClimbViewController', function ($scope, $stateParams, Climb) {
    $scope.Climb = Climb.get({ id: $stateParams.id });
});

var logbookApp = angular.module('logbookApp', ['ui.router', 'ngResource', 'logbookApp.controllers', 'logbookApp.services']);

logbookApp.config(function ($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/climbs');

    $stateProvider
        .state('climbs', {
            url:'/climbs',
            templateUrl: 'partials/climbs.html',
            //controller: 'ClimbListController'
        })
        .state('viewClimb', {
            url:'/climbs/:id/view',
            templateUrl: 'partials/climb-view.html',
            controller: 'ClimbViewController'
    })
})
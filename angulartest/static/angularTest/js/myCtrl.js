app.controller("myCtrl", function ($scope) {
    $scope.firstName = "Jed";
    $scope.lastName = "Thompson";
    $scope.todos = [
        'tidy room',
        'fix computer',
        'go climbing',
    ];

    $scope.done = function (todo) {
        var indexOf = $scope.todos.indexOf(todo);
        if (indexOf !== -1) {
            $scope.todos.splice(indexOf, 1);
        }
    }

    $scope.add = function (e) {
        if (e.which && e.which === 13) {
            $scope.todos.push($scope.newTodo);
            $scope.newTodo = "";
        }
    }

});
var app = angular.module('myApp', []);

app.controller('myController', ['$scope', '$http', function($scope, $http) {

    $scope.clickButton = function() {
        $http.get('http://127.0.0.1:5000/update').success(function(data) {
            $scope.greeting = data;
        });
    }

}]);
var mainApp = angular.module("mainApp", []);

mainApp.controller('tnt', ['$scope', function($scope) {
       $scope.Test = function($scope, $http) {
       	$http.get('http://127.0.0.1:5000/update').
        success(function(data) {
            $scope.greeting = data;
        }
    };
})]);



var app = angular.module('myApp', ['ngSanitize']);

app.controller('myController', ['$scope', '$http','$sce', function($scope, $http, $sce) {

    $scope.to_trusted = function(html_code) {
            return $sce.trustAsHtml(html_code);
    }

    $scope.clickButton = function() {
        $http.get('http://127.0.0.1:5000/update').success(function(data) {
            $scope.greeting = data;
    });
    }

    $scope.doSearch = function(query){
        $http({
            url: 'update',
            method: "POST",
            data: {search: query},
        }).success(function(data) {
            $scope.greeting = data;
        });
    }

    $scope.doTrailer = function(query){
        $http({
            url: 'trailer',
            method: "POST",
            data: {search: query},
        }).success(function(data) {
            $scope.trailers = data;
        });
    }



}]);

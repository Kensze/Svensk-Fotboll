var app = angular.module('myApp', ['ngSanitize'])

.filter('toTrusted', ['$sce', function($sce) {
    return function(text) {
        return $sce.trustAsHtml(text);
    };
}])

app.controller('myController', ['$scope', '$http','$location', '$window', '$sce',  function($scope, $http, $location, $window, $sce, $filter, $compile) {

// Hämtar IMDB-ID från URL:et i webbläsaren. 
    $scope.imdbID = function() {
        var pathname = $window.location.pathname.substring(1);
        var parts = pathname.split(/\//);
        if (parts.length > 1 ) {
            $scope.ID = parts[1];
        }
        $http.get('/movie/' + $scope.ID).success(function(data) {
            $scope.greeting = data;
    });
    }

// Hämtar IMDB-ID från URL:en i webbläsren och skickar det till /trailers/. Den får sedan tillbaka en Iframe.
/*
    $scope.imdbTrailer = function() {
        var pathname = $window.location.pathname.substring(1);
        var parts = pathname.split(/\//);
        if (parts.length > 1 ) {
            $scope.ID = parts[1];
        }
       $http.get('/trailer/' + $scope.ID).success(function(data) {
        $scope.trailer = data;
    });
    }

*/
// Den postar till /search/ och får tillbaka sökresultaten. 
    $scope.doSearch = function(query){
        $http({
            url: 'search',
            method: "POST",
            data: {search: query},
        }).success(function(data) {
            $scope.greeting = data;
        });
    }

    }]);

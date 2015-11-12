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

// Den postar till /search/ och får tillbaka sökresultaten. 
	$scope.doSearch = function(query){
			console.log(query)
		$http({
			url: 'search?q=' + query,
			method: "GET",
		}).success(function(data) {
			$scope.greeting = data;
		});
	}

	}]);

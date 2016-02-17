angular.module('blstApp').controller("MainController", function($rootScope, $scope, MainService){
    $scope.bucketlists = MainService.bucketlists.getBucketlists();

    $scope.$on('bucketlistChange', function () {
        $scope.bucketlists = MainService.bucketlists.getBucketlists();
    });

    $scope.add_bucketlist = function(){

        $scope.state = "create"

        bucketlist = {
            name: $scope.bucketlist.name
        }
        MainService.bucketlists.addBucketlist(bucketlist).
        $promise.
        then(function(result){
            $scope.$emit('bucketlistChange');
            $scope.bucketlist = {}
        }).
        catch(function(response){
            console.log("failed to add bucketlist");
        })
    }

    $scope.showCreateModal = function () {
        $rootScope.state = "create"
    }

    $scope.showEditModal = function (bid) {

        $rootScope.state = "update"

        $scope.editbucketlist = {}
        MainService.single_bucketlist.getBucketlist({id:bid}).
        $promise.
        then(function(result){
            $scope.editbucketlist = result;
        }).
        catch(function(response){
            console.log("failed to get bucketlist");
        })
    }

    $scope.update_bucketlist = function(params){
        MainService.single_bucketlist.updateBucketlist(params).
        $promise.
        then(function(result){
            $scope.$emit('bucketlistChange');
        }).
        catch(function(response){
            console.log("failed to update bucketlist");
        });

    }

    $scope.showItemModal = function(parent_id) {
        $rootScope.state = "add"
        $scope.parentbucketlist = {}

        MainService.single_bucketlist.getBucketlist({id:parent_id}).
        $promise.
        then(function(result){
            $scope.parentbucketlist = result;
        }).
        catch(function(response){
            console.log("failed to get bucketlist");
        })
    }

    $scope.add_item = function(itemparams){
        MainService.bucketlist_items.addItem(itemparams).
        $promise.
        then(function(result){
            $scope.item = {}
            $scope.$emit('bucketlistChange');
        }).
        catch(function(response){
            console.log("failed to add item");
        });
    }

    $scope.showDeleteModal = function (bid) {

        $rootScope.state = "delete"
        $scope.deletebucketlist = bid
    }

    $scope.delete_bucketlist = function(){
        MainService.single_bucketlist.deleteBucketlist({id:$scope.deletebucketlist}).
        $promise.
        then(function(result){
            $scope.$emit('bucketlistChange');
        }).
        catch(function(response){
            console.log("failed to delete bucketlist");
        })
    }
});

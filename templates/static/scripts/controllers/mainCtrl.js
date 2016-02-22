angular.module('blstApp').controller("MainController", function($rootScope, $scope, MainService){
    $scope.bucketlists = MainService.bucketlists.getBucketlists();

    $scope.$on('bucketlistChange', function () {
        $scope.bucketlists = MainService.bucketlists.getBucketlists();
        window.location.reload();
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
        });
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
        });
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
        });
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

    $scope.showDeleteModal = function(bid) {

        $rootScope.state = "remove"
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
        });
    }

    $scope.showItemEditModal = function(item) {
        $rootScope.state = "edit"
        $scope.item = item
    }

    $scope.update_item = function(params){
        item = {
            id: params.id || $scope.item.id,
            name: params.name || $scope.item.name,
            done: params.done || $scope.item.done,
            parent_bucketlist: params.parent_bucketlist || $scope.item.parent_bucketlist
        }
        MainService.item.updateItem(item).
        $promise.
        then(function(result){
            $scope.item = {}
            console.log("updated item");
        }).
        catch(function(response){
            console.log("failed to update item");
        });

    }
});

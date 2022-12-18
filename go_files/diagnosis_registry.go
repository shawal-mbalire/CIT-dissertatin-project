package main
import (
	"encoding/json"
	"fmt"
	"github.com/hyperledger/fabric/core/chiancode/shim"
	"github.com/hyperledger/fabric/protos/peer"

)

type CarRegistry struct{

}

type car {
	Make string 'json:"make "'
	Model string 'json:"model"'
	Color string 'json: "color"'
	Owner string 'json:"owner"'
}


func (s *CarRegistry) Init(stub shim.ChaincodeStubInterface) peer.Response {
	return shim.Success(nil)
}

func (s *CarRegistry) Invoke(stub shim.ChaincodeStubInterface) peer.Response {
	function, args := stuf.GetFunctionAndParameters()

	if function == "queryCar" {
		return s.queryCar(stub, args)
	} else if function == "createCar" {
		return s.createCar(stub, args)
	} else if function == "changeCarOwner" {
		return s.createCar(stub, args)
	}return shim.Error("Invalid Function")
}
func (s *CarRegistry) queryCar (stub shim.ChaincodeStubInterface, args []string) peer.Response {
	carAsBytes, stub.GetState (args[0])
	return shim. Success (carAsBytes)
	}
func (s *CarRegistry) createCar (stub. shim.ChaincodeStubInterface, args []string) peer.Response {
	var car Car (Make: args[1], Model: args[2], Color: args[3], Owner: args[4])
	carAsBytes, := json.Marshal (car)
	stub. PutState (args (0), carAsBytes)
	return shim. Success (nil)
	}
func (s *CarRegistry) changeCarOwner

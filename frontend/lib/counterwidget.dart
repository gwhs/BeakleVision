import 'package:flutter/material.dart';

class Counter extends StatefulWidget {
	const Counter({super.key});

	@override
	  State<Counter> createState() => CounterState();
}

class CounterState extends State<Counter> {
int counter = 0;
@override
  Widget build(BuildContext context) {
  
	return Row(
	mainAxisAlignment: MainAxisAlignment.center,
	children: [
	SizedBox(
	width: 50,
	height: 35,
	child: TextButton(onPressed: (){
	if (counter-- == 0) {
		  counter = counter;}
	else {
	setState(() {
		  counter--;
		});}
	}, 

	style: TextButton.styleFrom(
	backgroundColor: Colors.red,
	shape: RoundedRectangleBorder(
	borderRadius: BorderRadiusGeometry.only(
	bottomLeft: Radius.circular(25),
	topLeft: Radius.circular(25)
	),
	)
	),
	child: Text(
	"-",
	textScaler: TextScaler.linear(1.25),
	style: TextStyle(color: Colors.black),
	),
	)),
	Padding(padding: EdgeInsets.only(right: 5)),
	Text(
	"$counter",
	textScaler: TextScaler.linear(1.25),
	),
	Padding(padding: EdgeInsets.only(right: 5)),
	SizedBox(
	width: 50,
	height: 35,
	child: TextButton(onPressed: (){
	setState(() {
		  counter++;
		});
	}, 
	child: Text(
	"+",
	textScaler: TextScaler.linear(1.25),
	style: TextStyle(color: Colors.black),
	),
	style: TextButton.styleFrom( 
	backgroundColor: Colors.red, 
	shape: RoundedRectangleBorder( 
	borderRadius: BorderRadiusGeometry.only( 
	topRight: Radius.circular(100), 
	bottomRight: Radius.circular(100)
	)
	)
	),
	)
	)
	],
	);
	}

  int getcount() {
  return counter;
  }
}

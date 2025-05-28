

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
	TextButton(onPressed: (){
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
	borderRadius: BorderRadius.only(
	topLeft: Radius.circular(100),
	bottomLeft: Radius.circular(100)
	)
	)
	),
	child: Text(
	"-",
	textScaler: TextScaler.linear(1.5),
	style: TextStyle(color: Colors.black),
	),
	),
	Padding(padding: EdgeInsets.all(4)),
	Text("$counter"),
	Padding(padding: EdgeInsets.all(4)),
	TextButton(onPressed: (){
	setState(() {
		  counter++;
		});
	}, 
	style: TextButton.styleFrom(
	backgroundColor: Colors.red,
	shape: RoundedRectangleBorder(
	borderRadius: BorderRadius.only(
	topRight: Radius.circular(100),
	bottomRight: Radius.circular(100)
	)
	)
	),
	child: Text(
	"+",
	style: TextStyle(color: Colors.black),
	textScaler: TextScaler.linear(1.5),
	))
	],
	);
  }

  int getcount() {
  return counter;
  }
}

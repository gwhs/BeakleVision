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
	width: 30,
	height: 25,
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
	child: Icon(Icons.remove, color: Colors.black,),
	)),
	Padding(padding: EdgeInsets.only(right: 5)),
	Text(
	"$counter",
	textScaler: TextScaler.linear(1.25),
	),
	Padding(padding: EdgeInsets.only(right: 5)),
	SizedBox(
	width: 35,
	height: 25,
	child: TextButton(onPressed: (){
	setState(() {
		  counter++;
		});
	}, 
	style: TextButton.styleFrom( 
	backgroundColor: Colors.red, 
	shape: RoundedRectangleBorder( 
	borderRadius: BorderRadiusGeometry.only( 
	topRight: Radius.circular(100), 
	bottomRight: Radius.circular(100)
	)
	)
	),
	child: Icon(Icons.add, color: Colors.black,),
	)
	)
	],
	);
	}

  int getcount() {
  return counter;
  }
}

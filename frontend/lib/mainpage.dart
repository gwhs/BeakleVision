import 'package:flutter/material.dart';
import 'package:frontend/fullcounterwidget.dart';

class Mainpage extends StatelessWidget {
	const Mainpage({super.key});

	@override
	  Widget build(BuildContext context) {
	  
		return Scaffold(
		appBar: AppBar(
		title: Align(
		alignment: Alignment.center,
		child: Text("Beakle Vision")
		)
		),
		body: Align(
		alignment: Alignment.topCenter, 
		child: Column(
			children: [
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Auton L1"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Auton L2",)
			],
			),

			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Auton L3"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Auton L4",)
			],
			)
			],
		)
		),
		);	  
}
}

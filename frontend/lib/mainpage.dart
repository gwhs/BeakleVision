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
			),
			Padding(padding: EdgeInsets.all(10)),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Teleop L2"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Teleop L2")
			],
			),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Teleop L3"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Teleop L4",)
			],	
			),
			Padding(padding: EdgeInsets.all(10)),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Algae Processor"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Algae Barge")
			],
			),
			Padding(padding: EdgeInsetsGeometry.all(10)),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Speed"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Fouls")
			],
			),
			Padding(padding: EdgeInsetsGeometry.all(2)),			Center(child: Text("Defense", textScaler: TextScaler.linear(1.5),),),
			Center(child: Checkbox(value: false, onChanged: (bool? val){}),)
			],
		)
		),
		);	  
}
}

import 'package:flutter/material.dart';
import 'package:frontend/fullcounterwidget.dart';
import 'package:frontend/misswidget.dart';
import 'package:frontend/togglebutton.dart';

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
			Misswidget(),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Auton L3"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Auton L4",)
			],
			),
			Misswidget(),
			Padding(padding: EdgeInsets.all(5)),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Teleop L1"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Teleop L2")
			],
			),
			Misswidget(),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Teleop L3"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Teleop L4",)
			],	
			),
			Misswidget(),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Algae Processor"),
			Fullcounterwidget(title: "Algae Barge")
			],
			),
			Misswidget(),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Speed"),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Fouls")
			],
			),
			Togglebutton()
			],
		)
		),
		floatingActionButton: FloatingActionButton(onPressed: (){
		debugPrint("Upload");
		},
		child: Text("Done", style: TextStyle(color: Colors.black),),
		),
		);	  
}
}

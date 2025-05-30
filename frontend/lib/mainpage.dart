import 'package:flutter/material.dart';
import 'package:frontend/counterwidget.dart';
import 'package:frontend/fullcounterwidget.dart';
import 'package:frontend/misswidget.dart';
import 'package:frontend/togglebutton.dart';

class Mainpage extends StatelessWidget {
	

	final GlobalKey<CounterState> AL1 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL2 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL3 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL4 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL1M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL2M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL3M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> AL4M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL1 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL2 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL3 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL4 = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL1M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL2M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL3M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> TL4M = GlobalKey<CounterState>();
	final GlobalKey<CounterState> ALGP = GlobalKey<CounterState>();
	final GlobalKey<CounterState> ALGPM = GlobalKey<CounterState>();
	final GlobalKey<CounterState> ALGB = GlobalKey<CounterState>();
	final GlobalKey<CounterState> ALGBM = GlobalKey<CounterState>();
	final GlobalKey<CounterState> Speed = GlobalKey<CounterState>();
	final GlobalKey<CounterState> Fouls = GlobalKey<CounterState>();
	final GlobalKey<ToggleButtonState> DEFBOT = GlobalKey<ToggleButtonState>();

	Mainpage({super.key});
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
			Fullcounterwidget(title: "Auton L1", counterState: AL1,),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Auton L2", counterState: AL2,)
			],
			),
			Misswidget(keys: [AL1M, AL2M]),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Auton L3", counterState: AL3,),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Auton L4", counterState: AL4,)
			],
			),
			Misswidget(keys: [AL3M, AL4M]),
			Padding(padding: EdgeInsets.all(5)),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Teleop L1", counterState: TL1,),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Teleop L2", counterState: TL2,)
			],
			),
			Misswidget(keys: [TL1M, TL2M]),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Teleop L3", counterState: TL3,),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Teleop L4", counterState: TL4,)
			],	
			),
			Misswidget(keys: [TL3M, TL4M],),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Algae Processor", counterState: ALGP,),
			Padding(padding: EdgeInsetsGeometry.only(right: 5)),
			Fullcounterwidget(title: "Algae Barge", counterState: ALGB,)
			],
			),
			Misswidget(keys: [ALGPM, ALGBM],),
			Row(
			mainAxisAlignment: MainAxisAlignment.center,
			children: [
			Fullcounterwidget(title: "Speed", counterState: Speed,),
			Padding(padding: EdgeInsets.only(right: 10)),
			Fullcounterwidget(title: "Fouls", counterState: Fouls,)
			],
			),
			Togglebutton(key: DEFBOT,)
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

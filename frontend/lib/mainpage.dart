import 'package:flutter/material.dart';
import 'package:frontend/config.dart';
import 'package:frontend/counterwidget.dart';
import 'package:frontend/fullcounterwidget.dart';
import 'package:frontend/logic/sendtobackend.dart';
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
		Sendtobackend.sendtoback(getallfields());
		},
		child: Text("Done", style: TextStyle(color: Colors.black),),
		),
		);	  
}

Map<String, dynamic> getallfields() {
	int? al1 = AL1.currentState?.getcount();
	int? al1m = AL1M.currentState?.getcount();
	int? al2 = AL2.currentState?.getcount();
	int? al2m = AL2M.currentState?.getcount();
	int? al3 = AL3.currentState?.getcount();
	int? al3m = AL3M.currentState?.getcount();
	int? al4 = AL4.currentState?.getcount();
	int? al4m = AL4M.currentState?.getcount();
	int? tl1 = TL1.currentState?.getcount();
	int? tl1m = TL1M.currentState?.getcount();
	int? tl2 = TL2.currentState?.getcount();
	int? tl2m = TL2M.currentState?.getcount();
	int? tl3 = TL3.currentState?.getcount();
	int? tl3m = TL3M.currentState?.getcount();
	int? tl4 = TL4.currentState?.getcount();
	int? tl4m = TL4M.currentState?.getcount();
	int? algp = ALGP.currentState?.getcount();
	int? algpm = ALGPM.currentState?.getcount();
	int? algb = ALGB.currentState?.getcount();
	int? algbm = ALGBM.currentState?.getcount();
	int? speed = Speed.currentState?.getcount();
	int? fouls = Fouls.currentState?.getcount();
	return {
	"AL1": al1,
	"AL1M": al1m,
	"AL2": al2,
	"AL2M": al2m,
	"AL3": al3,
	"AL3M": al3m,
	"AL4": al4,
	"AL4M": al4m,
	"TL1": tl1,
	"TL1M": tl1m,
	"TL2": tl2,
	"TL2M": tl2m,
	"TL3": tl3,
	"TL3M": tl3m,
	"TL4": tl4,
	"TL4M": tl4m,
	"ALGP": algp,
	"ALGPM": algpm,
	"ALGB": algb,
	"ALGBM": algbm,
	"Fouls": fouls,
	"Speed": speed
	};
}
}

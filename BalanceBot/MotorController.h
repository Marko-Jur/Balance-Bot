#ifndef _PIN_ASSIGNMENTS_H
#define _PIN_ASSIGNMENTS_H

#include "Pin_Assignments.h"

#endif 



#ifndef _MICROCONTROLLER_H
#define _MICROCONTROLLER_H
	class Actuator {
	public:
		virtual void output(float outputLevel) = 0;
	};

    class MotorController : public Actuator
    {
    private:
        int m_enA = RIGHT_MOTOR_ENABLE;
        int m_enB = LEFT_MOTOR_ENABLE;
        int m_in1 = RIGHT_MOTOR_A;
        int m_in2 = RIGHT_MOTOR_B;
        int m_in3 = LEFT_MOTOR_A;
        int m_in4 = LEFT_MOTOR_B;

    public:
        MotorController();
        ~MotorController();
        MotorController(int enA, int enB, int in1, int in2, int in3, int in4);

        void output(float outputValue) override;

    private:
        void motorForward();
        void motorReverse();
        void setMotorSpeed(float outputValue);
        void motorSetup();

    };
#endif



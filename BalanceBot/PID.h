/*
Function: Motor Controller
Author: Harmandeep Singh Dubb
Input Parameters: error_angle
Output Parameters: None

Purpose: *Initializes balance bot with a taget vertical position, and then the balance bot maintains that position


*/

#ifndef _PID_H_
#define _PID_H_

//Function declarations
class PID {
	public:
		virtual double* pidOutput() = 0;
};

class BalancePID : public PID
{
private: 
	double m_kp, m_ki, m_kd;
	int m_sampleTime = 100;
	double *m_sensorOutput;
	double *m_pidOutput;
	double *m_setpoint;
	double i_sum = 0;
	long m_last_time;
	double m_last_error = 0;
	double* m_output;

public:
	BalancePID();
	~BalancePID();
	BalancePID(double* sensorOutput, double* pidOutput, double* setpoint, double kp, double ki, double kd);
	void setTunings(double, double, double);
	double* pidOutput() override;
	void Compute();
private:

};

#endif

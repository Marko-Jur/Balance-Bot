#include "PID.h"
#include "Arduino.h"

BalancePID::BalancePID(double* sensorOutput, double* pidOutput, double* setpoint, double kp, double ki, double kd)
	: m_sensorOutput(sensorOutput), m_setpoint(setpoint), m_pidOutput(pidOutput)
{
	m_last_time = millis();
	setTunings(kp, ki, kd);
}

BalancePID::~BalancePID() 
{

}

double* BalancePID::pidOutput()
{
	return m_pidOutput;
}

void BalancePID::setTunings(double kp, double ki, double kd)
{
	m_kp = kp;
	m_kd = kd;
	m_ki = ki;
}

void BalancePID::Compute()
{
	long time_delta = millis() - m_last_time;
  Serial.println(time_delta);
	if (time_delta <= m_sampleTime)
		return;
	m_last_time = millis();
	double error_angle = *m_sensorOutput - *m_setpoint;
	double p_term = error_angle * m_kp;
	i_sum = i_sum + (error_angle * m_ki);
	i_sum = (i_sum < 0) ? -(min(256.0, abs(i_sum))) : (min(256.0, abs(i_sum)));
	double d_term = (error_angle - m_last_error)/((double)(time_delta)) * m_kd;
  m_last_error = error_angle;
	double output = p_term + i_sum + d_term;
	*m_pidOutput = (output < 0) ? -(min(256.0, abs(output))) : (min(256.0, abs(output)));
}

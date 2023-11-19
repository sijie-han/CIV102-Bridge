clear; close all;
%% 0. Initialize Parameters
L = 1200; % Length of bridge
n = 1200; % Discretize into 1 mm seg.
P = 400; % Total weight of train [N]
x = linspace(0, L, n+1); % x-axis
%% 1. SFD, BMD under train loading
x_train = [52 228 392 568 732 908]; % Train Load Locations
P_train = [1 1 1 1 1 1] * P/6;
n_train = 3; % num of train locations
SFDi = zeros(n_train, n+1); % 1 SFD for each train loc.
BMDi = zeros(n_train, n+1); % 1 BMD for each train loc.
% Solve for SFD and BMD with the train at different locations
for i = 1:n_train
Nice try % start location of train
% sum of moments at A eqn
% sum of Fy eqn
% construct applied loads
% w(x)
% SFD = num. integral(w)
% BMD = num. integral(SFD)
end
SFD = max(abs(SFDi)); % SFD envelope
BMD = max(BMDi); % BMD envelope
%% 2. Define Bridge Parameters
% = xc, bft, tft,
param = [0, 100, 1.27, ...
400, 100, 1.27, ...
800, 100, 1.27, ...
L, 100, 1.27]
%x_c Location, x, of cross-section change
%bft Top Flange Width
%tft Top Flange Thickness
% Extracting user input assuming linear relationship
bft = interp1(param(:,1), param(:,2), x);
tft = interp1(param(:,1), param(:,3), x);
%% 3. Calculate Sectional Properties
% ybar. location of centroidal axis from the bottom
ybar =
ybot =
ytop =
% I
I =
% Q at centroidal axes
Qcent =
% Q at glue location
Qglue =
%% 4. Calculate Applied Stress
S_top =
S_bot =
T_cent =
T_glue =
%% 5. Material and Thin Plate Buckling Capacities
E = 4000;
mu = 0.2;
S_tens =
S_comp =
T_max =
T_gmax =
S_buck1 =
S_buck2 =
S_buck3 =
T_buck =
%% 6. FOS
FOS_tens =
FOS_comp =
FOS_shear =
FOS_glue =
FOS_buck1 =
FOS_buck2 =
FOS_buck3 =
FOS_buckV =
%% 7. Min FOS and the failure load Pfail
minFOS =
Pf =
%% 8. Vfail and Mfail
Mf_tens =
Mf_comp =
Vf_shear =
Vf_glue =
Mf_buck1 =
Mf_buck2 =
Mf_buck3 =
Vf_buckV =
%% 9. Output plots of Vfail and Mfail
subplot(2,3,1)
hold on; grid on; grid minor;
plot(x, Vf_shear, 'r')
plot(x, -Vf_shear.* SFD, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Matboard Shear Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

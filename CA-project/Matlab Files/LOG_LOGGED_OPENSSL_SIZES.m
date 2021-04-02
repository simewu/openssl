marker_size = 14;
line_width = 2;
font_size = 18;
bar_texts_font_size = 14;
%color = 'black'

disp('Begin');

data = readmatrix('NEW_LOGGED_OPENSSL3_PLUS_SIZES.csv');
data_str = readtable('NEW_LOGGED_OPENSSL3_PLUS_SIZES.csv');

algorithm_in_english = string(table2array(data_str(:,4)));

disp('Data read');

%ca_key = data(:,12); % "Private Key for CA"
csr = data(:,11); % "CSR"
%%%%%%%%%%%%%%%%%%crt = data(:,10); % "Certificate for End Entity"
ca_pem = data(:,13); % "Certificate for End Entity"
%ca_srl = data(:,14);
%combined_data = [csr, crt, ca_pem];
combined_data = [csr, ca_pem];

disp('Data in variables, plotting...');

y = combined_data;
b = bar(y);
%title('File Size Comparison', 'FontSize', font_size);

disp('Plotted, customizing...');

%axis square;
%xlabel('Algorithm', 'FontSize', font_size);
%xticklabels({'RSA 2048', 'RSA 3072', 'RSA 4096', 'Dilithium 2', 'Dilithium 3', 'Dilithium 4', 'Falcon 512', 'Falcon 1024', 'RSA 3072 - Dilithium 2', 'RSA 3072 - Dilithium 3', 'RSA 3072 - Falcon 512', 'P256 - Dilithium 2', 'P256 - Dilithium 3', 'P384 - Dilithium 4', 'P256 - Falcon 512'});
%xtickangle(20);
xticks(1:length(algorithm_in_english));
xticklabels(algorithm_in_english);
xtickangle(45);

ylabel('Storage Cost (bytes)', 'FontSize', font_size);
set(gca, 'YScale', 'log');
set(gca,'FontSize', font_size);
set(gca, 'YGrid', 'on', 'XGrid', 'off');
%set(gca,'YTickLabel',num2str(get(gca,'YTick').'));


set(gca,'ytick',[0 10 100 1000 10000 100000 1000000 10000000]);
ylim([749 100000000]);
%ylim([749 15000]);

disp('Drawing text...');

%concatenated = horzcat(crt', csr', ca_pem');
%h = text(1:length(crt'),crt'*1.1,num2str(crt),'vert','middle','horiz','left', 'FontSize', font_size); 
%disp(h)
%set(h,'Rotation', 90);

% Used when combined_data = [csr, crt, ca_pem];
%h1 = text((1:length(csr'))-0.25,csr'*1.01,num2str(round(csr*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
%set(h1,'Rotation', 90);
%h2 = text((1:length(crt')),crt'*1.01,num2str(round(crt*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
%set(h2,'Rotation', 90);
%h3 = text((1:length(ca_pem'))+0.25,ca_pem'*1.01,num2str(round(ca_pem*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
%set(h3,'Rotation', 90);

% Used when combined_data = [csr, ca_pem];
h2 = text((1:length(csr'))-0.23,csr'*1.01,num2str(round(csr*100)/100),'vert','middle','horiz','left', 'FontSize', bar_texts_font_size); 
set(h2,'Rotation', 90);
h3 = text((1:length(ca_pem'))+0.23,ca_pem'*1.01,num2str(round(ca_pem*100)/100),'vert','middle','horiz','left', 'FontSize', bar_texts_font_size); 
set(h3,'Rotation', 90);


disp('Drawing legend...');

%             When combined_data = [csr, crt, ca_pem];
%legend('CSR', 'Certificate for End Entity', 'Certificate for CA', 'Location', 'NorthWest');
% With extention: legend('CSR (.csr', 'Certificate for End Entity  (.crt)', 'Certificate for CA (.pem)', 'Location', 'NorthWest');

%             When combined_data = [csr, ca_pem];
legend('CSR', 'End Entity Certificate', 'Location', 'NorthWest');


width = 2500;
height = 600;
set(gcf,'position',[100,100,width,height])

disp('Done!');




marker_size = 14;
line_width = 2;
font_size = 12;
%color = 'black'

disp('Begin');

data = readmatrix('old_LOGGED_OPENSSL.csv');
xticklabels({'RSA 2048', 'RSA 3072', 'RSA 4096', 'Dilithium 2', 'Dilithium 3', 'Dilithium 4', 'Falcon 512', 'Falcon 1024', 'RSA 3072 - Dilithium 2', 'RSA 3072 - Dilithium 3', 'RSA 3072 - Falcon 512', 'P256 - Dilithium 2', 'P256 - Dilithium 3', 'P384 - Dilithium 4', 'P256 - Falcon 512'});

disp('Data read');

crt = data(:,9);
csr = data(:,10);
%ca_key = data(:,11);
ca_pem = data(:,12);
%ca_srl = data(:,13);
combined_data = [csr, crt, ca_pem];

disp('Data in variables, plotting...');

y = combined_data;
b = bar(y);
%title('File Size Comparison', 'FontSize', font_size);

disp('Plotted, customizing...');

%axis square;
%xlabel('Algorithm', 'FontSize', font_size);
xticklabels({'RSA 2048', 'RSA 3072', 'RSA 4096', 'Dilithium 2', 'Dilithium 3', 'Dilithium 4', 'Falcon 512', 'Falcon 1024', 'RSA 3072 - Dilithium 2', 'RSA 3072 - Dilithium 3', 'RSA 3072 - Falcon 512', 'P256 - Dilithium 2', 'P256 - Dilithium 3', 'P384 - Dilithium 4', 'P256 - Falcon 512'});
xtickangle(20);
ylabel('Storage Cost (bytes)', 'FontSize', font_size);
set(gca, 'YScale', 'log');
set(gca,'FontSize', font_size);
set(gca, 'YGrid', 'on', 'XGrid', 'off');
%set(gca,'YTickLabel',num2str(get(gca,'YTick').'));


set(gca,'ytick',[0 10 100 1000 10000]);
ylim([749 15000]);

disp('Drawing text...');

%concatenated = horzcat(crt', csr', ca_pem');
%h = text(1:length(crt'),crt'*1.1,num2str(crt),'vert','middle','horiz','left', 'FontSize', font_size); 
%disp(h)
%set(h,'Rotation', 90);

h1 = text((1:length(csr'))-0.25,csr'*1.01,num2str(round(csr*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
set(h1,'Rotation', 90);
h2 = text((1:length(crt')),crt'*1.01,num2str(round(crt*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
set(h2,'Rotation', 90);
h3 = text((1:length(ca_pem'))+0.25,ca_pem'*1.01,num2str(round(ca_pem*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
set(h3,'Rotation', 90);

disp('Drawing legend...');

legend('CSR', 'Certificate for End Entity', 'Certificate for CA', 'Location', 'NorthWest');
width = 600;
height = 800;
set(gcf,'position',[100,100,width,height])

disp('Done!');




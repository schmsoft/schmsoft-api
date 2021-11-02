# Generated by Django 3.2.7 on 2021-10-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_owner_identification_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.CharField(blank=True, choices=[('Accounting', 'Accounting, bookkeeping and tax preparation'), ('Agents', 'A professional representative in a business transaction such as real estate'), ('Agriculture', 'Farming, fishing, and related business'), ('Antiques and Collectables', 'Sales and appraisals of antiques and collectables'), ('Arts and Crafts', 'Artists, artisans and related businesses such as art and galleries'), ('Assets Management', 'Managing investment and assets such as property'), ('Automotive', 'Automotive repair, customization and services'), ('Beverages', 'Beverages manufacturing, wineries and distilleries'), ('Brokers', 'Buying or selling services such as insurance for clients'), ('Business Services', 'Business services such as outsourcing of processes and administrative procedures. For examples, asset appraisal services for financial institutions'), ('Child Care', 'Licensed child care centers, home child care and preschools'), ('Cleanig Services', 'Indoor and outdoor cleaning services'), ('Design', 'Design is a broad field that includes the design of digital works such websites and physical things such as interior design'), ('Distributor', 'A business model that involves buying in bulk and sellling in smaller units. Often involves importing & exporting'), ('Ecommerce', 'Selling goods and services using digital channels such as web'), ('Education and Training', 'Schools and training services'), ('Entertainment', 'Production and ditribution of entertainmnet such as films'), ('Fashion', 'Apparel, footwear and accessories and related businesses such as fashion designers and modeling agencies'), ('Food Sevices', 'Restuarants, cafes and catering'), ('Gardening and Landscaping', 'Gardening and landscaping services such as tree pruning'), ('Health and Beauty', 'Health and beauty services such as hair salons nails slon and spas'), ('Information Technology', 'A broad categories of business that includes software development, system integration, IT consulting, informaton secutrity and IT services'), ('Legal Services', 'Lawyers and legal services such as arbitration'), ('Maintenance and Repair', 'Maintenance and repair services for technology, machines, buildings, property and assets'), ('Management Services', 'Managing processes for individuals and businesses such as Managing rentals for property owner'), ('Manufacturing', 'Small scale manufacturing such as local souvenirs or a niche product'), ('Marketing Services', 'Advertising, promotion, sales and other marketing services'), ('Media', 'Production and distribution of media such as graphics and video'), ('Medical Practitioners', 'Doctors, dentists and other medical practitioners'), ('Music', 'Production, promotion and distribution of music'), ('Nightlife', 'Bars, nightclubs and other forms of nightlife such as karaoke'), ('Personal Services', 'Personal consulting services such as personal trainer'), ('Pet Services', 'Pet supplies and services such as grooming and training'), ('Photography', 'Photographers and Photography services'), ('Professional Services', 'Consulting and freelancing'), ('Publishing', 'Publishing literature or informaton in physical or digital formats'), ('Recruiting and Staffing', 'Recruiters and staffing services'), ('Rental and Leasing', 'Reniting and leasing of property, vehicles, machines, electonics and other assets'), ('Research Services', 'Research services such as market research'), ('Retail', 'Selling products from physical location'), ('Shipping and Delivery', 'Shipping and delivery services such local delivery of takeout or flowers'), ('Sports and Recreation', 'Businesses that compete with far large competitor by applealing to customers who prioritize sustainable practices'), ('Toys and Hobbies', 'Production and distribution of toys and obby Products'), ('Transportation', 'Transportation related businesses such as bicycle rentals or taxis'), ('Travel and Tourism', 'Hotels, resorts, tours, travel agencies souvenirs vendors and other businesses related to tourism'), ('Value Added Reseller', 'A business model that involves reselling an existing product or services wrapped in a value added service. For example, selling software and adding implementation and support services'), ('Warehousing and Storage', 'Warehousing, moving and storage related businesses'), ('Wholesale', 'Buying and selling in bulk. Typically related to importing and exporting of goods')], max_length=255),
        ),
    ]
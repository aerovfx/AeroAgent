# 20 - Energy Efficient Computing translated

---

In this lecture, we'll explore how Nvidia's energy efficient computing can reduce environmental impact

while enhancing data center performance within the scope of the cert exam.

Modern applications, especially AI, demand unprecedented computing power,

driving up energy consumption in data centers. Effective planning and deployment require

balancing three critical resources, power, cooling and space, a change in one affects the other two,

making resource optimization essential for efficiency. For example, accelerated computing with

GPUs requires less physical space and achieves faster processing than traditional CPU-based systems

reducing energy use over time despite higher instantaneous power consumption.

Key technologies for energy efficiency include GPUs which are optimized for performance and

efficiency. Nvidia GPUs are designed to handle compute intensive workloads more efficiently than

CPUs, multi-instance GPUs or MIGs, partition GPUs to run multiple workloads simultaneously

without increasing power consumption. The efficiency gains are significant. A hyper scale data center

within video GPUs requires just one-forty-seventh of the rack space and 93% less energy compared to

equivalent CPU-based systems. For example, the DGX-H100 system runs AI models with a fraction of the

energy cost, offering extreme performance while maintaining minimal environmental impact.

Software optimization for AI workloads is another crucial aspect. Nvidia continuously

refines CUDAX libraries and GPU-excelerated applications to maximize energy efficiency.

Performance boosts are notable. AI workloads on the Nvidia Ampere architecture have improved by

two and a half times over two years. NGC energy savings are also impressive. Workloads

optimized through NGC or Nvidia GPU cloud save an estimated 20% in energy consumption.

Data processing units or DPUs are specialized processors designed to handle communication tasks.

By offloading these tasks from CPUs, DPUs can reduce their workload by 30% or more.

This efficiency means that fewer servers are needed to manage larger workloads,

which can lead to a significant reduction in data center power consumption,

up to four megawatts in fact. Advanced cooling solutions are crucial for maintaining performance

while minimizing energy usage in data centers. Nvidia employs some pretty cutting-edge technologies

to manage heat output. First, there's direct air cooling, which is cost-effective,

but can only cool up to 30 kilowatts per rack. Then we have water-cooled heat exchanges,

which are more efficient for high-density cooling, supporting up to 60 kilowatts per rack.

Finally, rear-door heat exchanges transfer heat from servers to chilled water,

enhancing cooling for slab floor facilities. For example, Nvidia's DGX-H100 system

uses physics-informed neural networks or pins to design optimized heat sinks.

This ensures peak performance with minimal cooling energy, quite impressive, isn't it?

Collocation simplifies deployment and enhances efficiency,

especially for businesses that don't have the infrastructure to support modern data centers.

Nvidia's DGX-ready data center program helps enterprises deploy high-performance AI solutions

without the need for extensive facilities planning. The benefits are clear.

It avoids the high costs and latency of public cloud solutions,

enabling rapid deployment with minimal operational complexity.

The program has a global reach available in regions like North America, Europe, Asia, and more.

Plus, it includes a partner ecosystem with storage and networking solutions from companies like

DDN, IBM, and NetApp. For example, a financial institution deployed Nvidia DGX systems in a

collocation facility. This move accelerated their AI workloads while reducing power and space

requirements. Pretty efficient, right? Energy efficiency gains with next-gen GPUs are substantial.

Each generation of Nvidia GPUs brings significant improvements. Take the hopper versus Ampere,

for instance. The H100 GPU offers three and a half times better energy efficiency than its

predecessor. This reduces the total cost of ownership while managing the same workload with fewer

servers. The performance advantage is also noteworthy. A 50 node HGX-H100 Supercomputer uses 2.6

GW annually compared to 12.1 GW for a comparable CPU system with 1,150 servers.

Nvidia is also designing for a NetZero data center. Their goal is to achieve this by optimizing

hardware, cooling, and operational practices. Features like TF32 Math Mode in Ampere GPUs and

reduced heat output enable faster, more efficient AI training while minimizing environmental impact.

So, to summarize the key takeaways on energy efficiency, optimized hardware reduces energy

consumption while delivering superior performance, advanced cooling systems like water-cooled heat

exchanges, enhanced efficiency in high-density environments. Collocation simplifies deployment

and provides scalable cost-effective solutions. And with each new GPU generation,

power requirements and operational costs continue to drop. With these strategies, Nvidia empowers

organizations to build efficient, sustainable data centers capable of meeting the growing demands of AI.
<!-- 
  Reference: https://element-plus.gitee.io/
-->
<template>
  <!-- 首页 -->
  <div class="common-layout">
    <el-container>
      <!-- 顶部栏 -->
      <el-header>
        <el-row :span="24" class="header">
          <el-col :span="10" class="logo">
            SDU 3D-Viewer
          </el-col>
          <el-col :span="6"></el-col>
          <el-col :span="8" class="userinfo">
            <div style="display: flex; margin-left: 40px;">
              <a href="https://github.com/HMTCuro/3D-Reconstruction" style="margin-right: 25px;">
                <div style="display: flex;">
                  <div style="margin-top: 10px; margin-right: 12px;">
                    <svg t="1644928889893" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3028" width="40" height="40"><path d="M960 512c0 97.76-28.704 185.216-85.664 263.264-56.96 78.016-130.496 131.84-220.64 161.856-10.304 1.824-18.368 0.448-22.848-4.032a22.4 22.4 0 0 1-7.2-17.504v-122.88c0-37.632-10.304-65.44-30.464-82.912a409.856 409.856 0 0 0 59.616-10.368 222.752 222.752 0 0 0 54.72-22.816c18.848-10.784 34.528-23.36 47.104-38.592 12.544-15.232 22.848-35.904 30.912-61.44 8.096-25.568 12.128-54.688 12.128-87.904 0-47.072-15.232-86.976-46.208-120.16 14.368-35.456 13.024-74.912-4.48-118.848-10.752-3.616-26.432-1.344-47.072 6.272a301.44 301.44 0 0 0-53.824 25.568l-21.984 13.888A407.776 407.776 0 0 0 512 280.16c-38.56 0-75.776 4.928-112.096 15.232a444.48 444.48 0 0 0-24.672-15.68c-10.336-6.272-26.464-13.888-48.896-22.432-21.952-8.96-39.008-11.232-50.24-8.064-17.024 43.936-18.368 83.424-4.032 118.848-30.496 33.632-46.176 73.536-46.176 120.608 0 33.216 4.032 62.336 12.128 87.456 8.032 25.12 18.368 45.76 30.496 61.44 12.544 15.68 28.224 28.704 47.072 39.04 18.848 10.304 37.216 17.92 54.72 22.816a409.6 409.6 0 0 0 59.648 10.368c-15.712 13.856-25.12 34.048-28.704 60.064a99.744 99.744 0 0 1-26.464 8.512 178.208 178.208 0 0 1-33.184 2.688c-13.024 0-25.568-4.032-38.144-12.544-12.544-8.512-23.296-20.64-32.256-36.32a97.472 97.472 0 0 0-28.256-30.496c-11.232-8.064-21.088-12.576-28.704-13.92l-11.648-1.792c-8.096 0-13.92 0.928-17.056 2.688-3.136 1.792-4.032 4.032-2.688 6.72 1.344 2.688 3.136 5.408 5.376 8.096 2.24 2.688 4.928 4.928 7.616 7.168l4.032 2.688c8.544 4.032 17.056 11.232 25.568 21.984 8.544 10.752 14.368 20.64 18.4 29.6l5.824 13.44c4.928 14.816 13.44 26.912 25.568 35.872 12.096 8.992 25.088 14.816 39.008 17.504 13.888 2.688 27.36 4.032 40.352 4.032 12.992 0 23.776-0.448 32.288-2.24l13.472-2.24c0 14.784 0 32.288 0.416 52.032 0 19.744 0.48 30.496 0.48 31.392a22.624 22.624 0 0 1-7.648 17.472c-4.928 4.48-12.992 5.824-23.296 4.032-90.144-30.048-163.68-83.84-220.64-161.888C92.256 697.216 64 609.312 64 512c0-81.152 20.192-156.064 60.096-224.672a445.184 445.184 0 0 1 163.232-163.232C355.936 84.192 430.816 64 512 64s156.064 20.192 224.672 60.096a445.184 445.184 0 0 1 163.232 163.232C939.808 355.488 960 430.848 960 512" fill="#ffffff" p-id="3029"></path></svg>
                  </div>
                  <div style="font-weight: bold;">GitHub</div>
                </div>
              </a>
              <a href="https://b23.tv/n1nB3VV" style="margin-right: 13px;">
                <div style="display: flex;">
                  <div style="margin-top: 3px; margin-right: 15px;">
                    <svg t="1644929158315" class="icon" viewBox="0 0 2299 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="951" width="54" height="54"><path d="M1775.840814 322.588002c6.0164 1.002733 53.144869-9.525967 55.150336-6.016401 3.0082 4.5123 24.065601 155.92504 18.550567 156.927774s-44.621635 10.027334-44.621635 10.027334c-3.0082-20.556034-28.577901-147.903173-29.079268-160.938707m75.205003-14.539634l20.556034 162.944174c10.5287-0.501367 53.144869-3.509567 57.155803-4.010934-6.0164-61.668103-16.545101-158.933241-16.545101-158.93324-20.054668-4.010934-41.112069-4.010934-61.166736 0m-40.610702 226.116376s92.752838-23.564234 126.344406-12.0328c17.046467 61.668103 48.131202 407.611118 51.139402 421.649386-21.057401 2.506833-90.246004 8.523234-95.761037 10.027333-4.5123-26.071068-81.72277-403.098818-81.722771-419.643919m343.436183-207.565809c5.515034 1.5041 54.648969-5.013667 55.150335-1.5041 1.002733 12.032801 6.0164 157.42914 0.501367 157.930507s-44.621635 4.010934-44.621635 4.010934c-1.002733-20.054668-12.032801-146.90044-11.030067-160.437341m75.70637-4.010933l4.010933 160.938707c10.5287 0 52.643502 2.506833 57.155803 2.005467-1.002733-61.668103 0-158.933241 0-158.933241-20.054668-3.509567-40.610702-5.013667-61.166736-4.010933m-64.676303 216.089043s94.758304-12.534167 126.845772 2.506833c7.019134 72.196803 6.0164 408.613852 7.019134 422.652119-21.558768 0-90.246004 1.002733-95.761038 2.005467-1.002733-26.071068-39.607968-410.619319-38.103868-427.164419m-220.099977-413.627519c54.648969 278.759879 96.262404 755.058234 97.766504 785.641602 0 0 43.117535 1.002733 91.750105 4.010934C2105.740095 614.383415 2070.644427 134.575493 2071.145794 119.033126c-12.032801-13.536901-126.344406 6.0164-126.344406 6.0164m-120.328005 659.297196c-10.5287-78.213204-290.291313-166.955108-447.720454-138.377206 0 0-19.553301-172.470141-27.073801-339.425248-6.517767-143.390873-1.002733-282.770813 0.501366-305.833681-10.5287-7.5205-123.837572 46.627102-185.004308 69.188603 0 0 73.199537 309.844614 126.344406 952.59671 0 0 84.730971 9.0246 230.12731-19.051934s317.365114-115.815705 302.825481-219.097244m-341.932083 140.88404l-24.566967-176.982441c6.0164-3.0082 156.927774 53.144869 172.971507 63.172203-2.506833 11.030067-148.40454 113.810238-148.40454 113.810238M610.664628 322.588002c6.0164 1.002733 53.144869-9.525967 55.150335-6.016401 3.0082 4.5123 24.065601 155.92504 18.550568 156.927774s-44.621635 10.027334-44.621635 10.027334c-3.0082-20.556034-28.577901-147.903173-29.079268-160.938707m75.205003-14.539634l20.556034 162.944174c10.5287-0.501367 53.144869-3.509567 57.155803-4.010934-6.517767-61.668103-16.545101-158.933241-16.545101-158.93324-20.054668-4.010934-41.112069-4.010934-61.166736 0m-40.610702 226.116376s92.752838-23.564234 126.344406-12.0328c17.046467 61.668103 48.131202 407.611118 51.139402 421.649386-21.057401 2.506833-90.246004 8.523234-95.761037 10.027333-4.5123-26.071068-81.72277-403.098818-81.722771-419.643919m343.436182-207.565809c5.515034 1.5041 54.648969-5.013667 55.150336-1.5041 1.002733 12.032801 6.0164 157.42914 0.501367 157.930507s-44.621635 4.010934-44.621635 4.010934c-1.002733-20.054668-11.531434-146.90044-11.030068-160.437341m75.706371-4.010933l4.010933 160.938707c10.5287 0 52.643502 2.506833 57.155803 2.005467-1.002733-61.668103 0-158.933241 0-158.933241-20.054668-3.509567-40.610702-4.5123-61.166736-4.010933m-64.676303 216.089043s94.758304-12.534167 126.845772 2.506833c7.019134 72.196803 6.0164 408.613852 7.019134 422.652119-21.558768 0-90.246004 1.002733-95.761038 2.005467-0.501367-26.071068-39.607968-410.619319-38.103868-427.164419m-220.099977-413.627519c54.648969 278.759879 96.262404 755.058234 97.766504 785.641602 0 0 43.117535 1.002733 91.750105 4.010934-28.577901-300.318647-63.67357-780.126569-63.172203-796.170303-12.032801-13.035534-126.344406 6.517767-126.344406 6.517767m-120.328005 659.297196c-10.5287-78.213204-290.291313-166.955108-447.720454-138.377206 0 0-19.553301-172.470141-27.073801-339.425248-6.517767-143.390873-1.002733-282.770813 0.501366-305.833681C174.475608-6.308547 61.166736 47.337689 0 69.89919c0 0 73.199537 309.844614 126.344406 952.59671 0 0 84.730971 9.0246 230.12731-19.051934s317.365114-115.815705 302.825481-219.097244m-341.932083 140.88404l-24.566967-176.982441c6.0164-3.0082 156.927774 53.144869 172.971507 63.172203-2.506833 11.030067-148.40454 113.810238-148.40454 113.810238" p-id="952" fill="#ffffff"></path></svg>
                  </div>
                  <div style="font-weight: bold;">三维重建</div>
                </div>
              </a>
              <a href="https://b23.tv/" style="margin-right: 0px;">
                <div style="display: flex;">
                  <div style="font-weight: bold;">网站开发</div>
                </div>
              </a>
            </div>
          </el-col>
        </el-row>
      </el-header>

      <!-- 主容器 -->
      <el-container>
        <!-- 侧栏 -->
        <el-aside width="200px">
          <el-menu
            active-text-color="#ffd04b"
            background-color="#20232c"
            class="el-menu-vertical-demo"
            default-active="0"
            text-color="#fff"
          >
            <!-- <el-sub-menu index="1" @click="clickMenuItem(1)">
              <template #title>
                <span class="menuTitle">点云</span>
              </template>
              <el-menu-item index="1-1">item one</el-menu-item>
              <el-menu-item index="1-2">item one</el-menu-item>
            </el-sub-menu> -->
            <el-menu-item index="0" @click="clickMenuItem(0)">
              <span class="menuTitle">点云</span>
            </el-menu-item>
            <el-menu-item index="1" @click="clickMenuItem(1)">
              <span class="menuTitle">点云（窗户识别）</span>
            </el-menu-item>
            <el-menu-item index="2" @click="clickMenuItem(2)">
              <span class="menuTitle">点云（语义分割）</span>
            </el-menu-item>
            <el-menu-item index="3" @click="clickMenuItem(3)">
              <span class="menuTitle">网格（表面重建）</span>
            </el-menu-item>
            <el-menu-item index="4" @click="clickMenuItem(4)">
              <span class="menuTitle">白模</span>
            </el-menu-item>
            <el-menu-item index="5" @click="clickMenuItem(5)">
              <span class="menuTitle">白模（使用Neus生成）</span>
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-container>
          <!-- 主要内容 -->
          <el-main>
            <div style="padding: 20px;">
              <el-scrollbar>
                <!-- 点云 -->
                <div v-show="onShow === 0">
                  <div class="leftTitle">点云</div>
                  <!-- 技术路线 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">技术路线</div>
                  <el-card class="box-card">
                    <div style="margin-top: 30px; margin-bottom: 20px;">
                      <el-steps :active="4" align-center finish-status="process">
                        <el-step title="Colmap" description="SFM"></el-step>
                        <el-step title="AA-RMVSNet" description="Estimate depth maps"></el-step>
                        <el-step title="Fusion" description="Generate point cloud"></el-step>
                        <el-step title="Potree" description="Render"></el-step>
                      </el-steps>
                    </div>  
                  </el-card>
                  <!-- 在线浏览 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 50px;">在线浏览</div>
                  <el-row :gutter="70" style="margin-left: 0px; margin-right: 0px; margin-top: 10px; margin-bottom: 40px;">
                    <el-col v-for="(o, index) in 3" :key="o" :xs="8" :sm="8" :md="8" :lg="8" :xl="2">
                      <a :href="getUrl(onShow, index)">
                        <el-card :body-style="{ padding: '0px' }" shadow="always" class="cardClass">
                          <div class="imgHoverZoom">
                            <img :src="getImg(onShow, index)" class="image" />
                          </div>
                          <div class="cardTitle"> {{ list[onShow][index].name }} </div>
                          <div style="padding: 0px">
                            <div class="bottom">
                              <div style="align-items: left;">
                                <el-tag class="ml-2" effect="dark" size="large" style="margin-right: 8px; background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].size}} </el-tag>
                                <!-- <el-tag class="ml-2" effect="dark" size="large" style="background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].points}}Points </el-tag>   -->
                              </div>
                              <div style="align-items: right;">
                                <a :href="getGithub(onShow, index)">
                                  <el-button type="primary" style="background-color: #20232c; border-color: #20232c; color: #ffd04b; font-weight: 400;">下载</el-button>
                                </a>
                              </div>
                            </div>
                          </div>
                        </el-card>
                      </a>
                    </el-col>
                  </el-row>
                </div>
  
                <!-- 点云（窗户识别） -->
                <div v-show="onShow === 1">
                  <div class="leftTitle">点云（窗户识别）</div>
                  <!-- 技术路线 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">技术路线</div>
                  <el-card class="box-card">
                    <div style="margin-top: 30px; margin-bottom: 20px;">
                      <el-steps :active="6" align-center finish-status="process">
                        <el-step title="Colmap" description="SFM"></el-step>
                        <el-step title="AA-RMVSNet" description="Estimate depth maps"></el-step>
                        <el-step title="Fusion" description="Generate point cloud"></el-step>
                        <el-step title="Edge detection" description="Get detection result"></el-step>
                        <el-step title="Transformation" description="Map to point cloud"></el-step>
                        <el-step title="Potree" description="Render"></el-step>
                      </el-steps>
                    </div>  
                  </el-card>
                  <!-- 在线浏览 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 50px;">在线浏览</div>
                  <el-row :gutter="70" style="margin-left: 0px; margin-right: 0px; margin-top: 10px; margin-bottom: 40px;">
                    <el-col v-for="(o, index) in 3" :key="o" :xs="8" :sm="8" :md="8" :lg="8" :xl="2">
                      <a :href="getUrl(onShow, index)">
                        <el-card :body-style="{ padding: '0px' }" shadow="always" class="cardClass">
                          <div class="imgHoverZoom">
                            <img :src="getImg(onShow, index)" class="image" />
                          </div>
                          <div class="cardTitle"> {{ list[onShow][index].name }} </div>
                          <div style="padding: 0px">
                            <div class="bottom">
                              <div style="align-items: left;">
                                <el-tag class="ml-2" effect="dark" size="large" style="margin-right: 8px; background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].size}} </el-tag>
                                <!-- <el-tag class="ml-2" effect="dark" size="large" style="background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].points}}points </el-tag>   -->
                              </div>
                              <div style="align-items: right;">
                                <a :href="getGithub(onShow, index)">
                                  <el-button type="primary" style="background-color: #20232c; border-color: #20232c; color: #ffd04b; font-weight: 400;">下载</el-button>
                                </a>
                              </div>
                            </div>
                          </div>
                        </el-card>
                      </a>
                    </el-col>
                  </el-row>
                </div>
  
                <!-- 点云（语义分割） -->
                <div v-show="onShow === 2">
                  <div class="leftTitle">点云（语义分割）</div>
                  <!-- 技术路线 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">技术路线</div>
                  <el-card class="box-card">
                    <div style="margin-top: 30px; margin-bottom: 20px;">
                      <el-steps :active="5" align-center finish-status="process">
                        <el-step title="Colmap" description="SFM"></el-step>
                        <el-step title="AA-RMVSNet" description="Estimate depth maps"></el-step>
                        <el-step title="ResNest" description="Semantic Segmentation"></el-step>
                        <el-step title="Fusion" description="Generate point cloud with segmentation result"></el-step>
                        <el-step title="Potree" description="Render"></el-step>
                      </el-steps>
                    </div>  
                  </el-card>
                  <!-- 在线浏览 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 50px;">在线浏览</div>
                  <el-row :gutter="70" style="margin-left: 0px; margin-right: 0px; margin-top: 10px; margin-bottom: 40px;">
                    <el-col v-for="(o, index) in 3" :key="o" :xs="8" :sm="8" :md="8" :lg="8" :xl="2">
                      <a :href="getUrl(onShow, index)">
                        <el-card :body-style="{ padding: '0px' }" shadow="always" class="cardClass">
                          <div class="imgHoverZoom">
                            <img :src="getImg(onShow, index)" class="image" />
                          </div>
                          <div class="cardTitle"> {{ list[onShow][index].name }} </div>
                          <div style="padding: 0px">
                            <div class="bottom">
                              <div style="align-items: left;">
                                <el-tag class="ml-2" effect="dark" size="large" style="margin-right: 8px; background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].size}} </el-tag>
                                <!-- <el-tag class="ml-2" effect="dark" size="large" style="background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].points}}points </el-tag>   -->
                              </div>
                              <div style="align-items: right;">
                                <a :href="getGithub(onShow, index)">
                                  <el-button type="primary" style="background-color: #20232c; border-color: #20232c; color: #ffd04b; font-weight: 400;">下载</el-button>
                                </a>
                              </div>
                            </div>
                          </div>
                        </el-card>
                      </a>
                    </el-col>
                  </el-row>
                </div>
  
                <!-- 网格（表面重建） -->
                <div v-show="onShow === 3">
                  <div class="leftTitle">网格（表面重建）</div>
                  <!-- 技术路线 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">技术路线</div>
                  <el-card class="box-card">
                    <div style="margin-top: 30px; margin-bottom: 20px;">
                      <el-steps :active="5" align-center finish-status="process">
                        <el-step title="Colmap" description="SFM"></el-step>
                        <el-step title="Colmap" description="Dense reconstruction"></el-step>
                        <el-step title="Meshlab" description="Surface reconstruction"></el-step>
                        <el-step title="Meshlab" description="Texture mapping"></el-step>
                        <el-step title="Three.js" description="Render"></el-step>
                      </el-steps>
                    </div>  
                  </el-card>
                  <!-- 在线浏览 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 50px;">在线浏览</div>
                  <el-row :gutter="70" style="margin-left: 0px; margin-right: 0px; margin-top: 10px; margin-bottom: 40px;">
                    <el-col v-for="(o, index) in 3" :key="o" :xs="8" :sm="8" :md="8" :lg="8" :xl="2">
                      <el-card :body-style="{ padding: '0px' }" shadow="always" class="cardClass" @click="onClick(onShow, index)">
                        <div class="imgHoverZoom">
                          <img :src="getImg(onShow, index)" class="image" />
                        </div>
                        <div class="cardTitle"> {{ list[onShow][index].name }} </div>
                        <div style="padding: 0px">
                          <div class="bottom">
                            <div style="align-items: left;">
                              <el-tag class="ml-2" effect="dark" size="large" style="margin-right: 8px; background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].size}} </el-tag>
                              <!-- <el-tag class="ml-2" effect="dark" size="large" style="background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].points}}points </el-tag>   -->
                            </div>
                            <div style="align-items: right;">
                              <a :href="getGithub(onShow, index)">
                                <el-button type="primary" style="background-color: #20232c; border-color: #20232c; color: #ffd04b; font-weight: 400;">下载</el-button>
                              </a>
                            </div>
                          </div>
                        </div>
                      </el-card>
                    </el-col>
                  </el-row>
                </div>
  
                <!-- 白模 -->
                <div v-show="onShow === 4">
                  <div class="leftTitle">白模</div>
                  <!-- 技术路线 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">技术路线</div>
                  <el-card class="box-card">
                    <div style="margin-top: 30px; margin-bottom: 20px;">
                      <el-steps :active="4" align-center finish-status="process">
                        <el-step title="Colmap" description="SFM"></el-step>
                        <el-step title="Colmap" description="Dense reconstruction"></el-step>
                        <el-step title="Meshlab" description="Surface reconstruction"></el-step>
                        <el-step title="Three.js" description="Render"></el-step>
                      </el-steps>
                    </div>  
                  </el-card>
                  <!-- 在线浏览 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 50px;">在线浏览</div>
                  <el-row :gutter="70" style="margin-left: 0px; margin-right: 0px; margin-top: 10px; margin-bottom: 40px;">
                    <el-col v-for="(o, index) in 3" :key="o" :xs="8" :sm="8" :md="8" :lg="8" :xl="2">
                      <el-card :body-style="{ padding: '0px' }" shadow="always" class="cardClass" @click="onClick(onShow, index)">
                        <div class="imgHoverZoom">
                          <img :src="getImg(onShow, index)" class="image" />
                        </div>
                        <div class="cardTitle"> {{ list[onShow][index].name }} </div>
                        <div style="padding: 0px">
                          <div class="bottom">
                            <div style="align-items: left;">
                              <el-tag class="ml-2" effect="dark" size="large" style="margin-right: 8px; background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].size}} </el-tag>
                              <!-- <el-tag class="ml-2" effect="dark" size="large" style="background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].points}}points </el-tag>   -->
                            </div>
                            <div style="align-items: right;">
                              <a :href="getGithub(onShow, index)">
                                <el-button type="primary" style="background-color: #20232c; border-color: #20232c; color: #ffd04b; font-weight: 400;">下载</el-button>
                              </a>
                            </div>
                          </div>
                        </div>
                      </el-card>
                    </el-col>
                  </el-row>
                </div>
  
                <!-- 白模（使用Neus生成） -->
                <div v-show="onShow === 5">
                  <div class="leftTitle">白模（使用Neus生成）</div>
                  <!-- 技术路线 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">技术路线</div>
                  <el-card class="box-card">
                    <div style="margin-top: 30px; margin-bottom: 20px;">
                      <el-steps :active="5" align-center finish-status="process">
                        <el-step title="Colmap" description="SFM"></el-step>
                        <el-step title="Mask" description="Dense reconstruction"></el-step>
                        <el-step title="Neus" description="Train"></el-step>
                        <el-step title="Extract Mesh" description="Extract surface from trained model"></el-step>
                        <el-step title="Three.js" description="Render"></el-step>
                      </el-steps>
                    </div>  
                  </el-card>
                  <!-- 在线浏览 -->
                  <div style="font-size: 28px; font-weight: bold; margin-top: 50px;">在线浏览</div>
                  <el-row :gutter="70" style="margin-left: 0px; margin-right: 0px; margin-top: 10px; margin-bottom: 40px;">
                    <el-col v-for="(o, index) in 3" :key="o" :xs="8" :sm="8" :md="8" :lg="8" :xl="2">
                      <el-card :body-style="{ padding: '0px' }" shadow="always" class="cardClass" @click="onClick(onShow, index)">
                        <div class="imgHoverZoom">
                          <img :src="getImg(onShow, index)" class="image" />
                        </div>
                        <div class="cardTitle"> {{ list[onShow][index].name }} </div>
                        <div style="padding: 0px">
                          <div class="bottom">
                            <div style="align-items: left;">
                              <el-tag class="ml-2" effect="dark" size="large" style="margin-right: 8px; background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].size}} </el-tag>
                              <!-- <el-tag class="ml-2" effect="dark" size="large" style="background-color: #20232c; border-color: #20232c;"> {{ list[onShow][index].points}}points </el-tag>   -->
                            </div>
                            <div style="align-items: right;">
                              <a :href="getGithub(onShow, index)">
                                <el-button type="primary" style="background-color: #20232c; border-color: #20232c; color: #ffd04b; font-weight: 400;">下载</el-button>
                              </a>
                            </div>
                          </div>
                        </div>
                      </el-card>
                    </el-col>
                  </el-row>
                </div>
                <el-backtop />
              </el-scrollbar>
            </div>
          </el-main>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Index',

  data: () => ({
    publicPath: import.meta.env.BASE_URL,
    onShow: 0,
    list: [
      [
        {name: "东北亚学院", size: "731.13MB", points: '51,109,820', img: "./src/assets/dongbeiya.png", url: "../potree/dongbeiya.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/1/dongbeiya.ply"},
        {name: "体育馆北馆", size: "707.89MB", points: '49,485,294', img: "./src/assets/gym_north.png", url: "../potree/gym_north.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/1/gym_north.ply"},
        {name: "体育馆南馆", size: "696.19MB", points: '48,667,291', img: "./src/assets/gym_south.png", url: "../potree/gym_south.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/1/gym_south.ply"}
      ],
      [
        {name: "东北亚学院", size: "1.76GB",   points: '', img: "./src/assets/dongbeiya_window.png", url: "../potree/dongbeiya_window.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/2/dongbeiya_window.ply"},
        {name: "体育馆北馆", size: "808.63MB", points: '', img: "./src/assets/gym_north_window.png", url: "../potree/gym_north_window.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/2/gym_north_window.ply"},
        {name: "体育馆南馆", size: "627.31MB", points: '', img: "./src/assets/gym_south_window.png", url: "../potree/gym_south_window.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/2/gym_south_window.ply"}
      ],
      [
        {name: "东北亚学院", size: "840.14MB", points: '', img: "./src/assets/dongbeiya_seg.png", url: "../potree/dongbeiya_seg.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/3/dongbeiya_seg.ply"},
        {name: "体育馆北馆", size: "661.26MB", points: '', img: "./src/assets/gym_north_seg.png", url: "../potree/gym_north_seg.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/3/gym_north_seg.ply"},
        {name: "体育馆南馆", size: "622.08MB", points: '', img: "./src/assets/gym_south_seg.png", url: "../potree/gym_south_seg.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/3/gym_south_seg.ply"}
      ],
      [
        {name: "东北亚学院", size: "27.58MB", points: '', img: "./src/assets/dongbeiya_tex.png", url: "../potree/dongbeiya.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/6/dongbeiya.ply"},
        {name: "体育馆北馆", size: "40.68MB", points: '', img: "./src/assets/gym_north_tex.png", url: "../potree/gym_north.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/6/gym_north.ply"},
        {name: "体育馆南馆", size: "36.30MB", points: '', img: "./src/assets/gym_south_tex.png", url: "../potree/gym_south.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/6/gym_south.ply"}
      ],
      [
        {name: "东北亚学院", size: "19.12MB", points: '', img: "./src/assets/dongbeiya_white.png", url: "../potree/dongbeiya.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/6/dongbeiya.ply"},
        {name: "体育馆北馆", size: "31.94MB", points: '', img: "./src/assets/gym_north_white.png", url: "../potree/gym_north.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/6/gym_north.ply"},
        {name: "体育馆南馆", size: "26.97MB", points: '', img: "./src/assets/gym_south_white.png", url: "../potree/gym_south.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/6/gym_south.ply"}
      ],
      [
        {name: "东北亚学院", size: "11.21MB", points: '', img: "./src/assets/dongbeiya_neus.png", url: "../potree/dongbeiya.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/7/dongbeiya_neus.ply"},
        {name: "体育馆北馆", size: "21.29MB", points: '', img: "./src/assets/gym_north_neus.png", url: "../potree/gym_north.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/7/gym_north_neus.ply"},
        {name: "体育馆南馆", size: "16.60MB", points: '', img: "./src/assets/gym_south_neus.png", url: "../potree/gym_south.html", github: "https://github.com/HMTCuro/3D-Reconstruction/releases/download/7/gym_south_neus.ply"}
      ],
    ],
  }),

  methods: {
    clickMenuItem(index) {
      this.onShow = index;
    },
    handleClick: function (tab, event) {
      console.log(tab, event);
    },
    getUrl: function (part, index) {
      return this.list[this.onShow][index].url;
    },
    getImg: function (part, index) {
      return this.list[this.onShow][index].img;
    },
    getGithub: function (part, index) {
      return this.list[this.onShow][index].github;
    },
    onClick: function (part, index) {
      this.$router.push({
        path: '/scene',
        name: 'Scene',
        params: {
          part: part - 3,
          index: index,
        },
      });
    },
  },
}
</script>

<style>
:root {
  --el-color-warning: #ffd04b;
}

body {
  margin: 0px;
}

.menuTitle {
  margin-left: 15px;
}

.leftTitle {
  font-family: '黑体';
  font-size: 36px;
  font-weight: bold;
  text-align: left;
  padding-top: 0px;
  margin-top: 30px;
  margin-left: 30px;
  margin-bottom: 10px;
}

.rightTitle {
  font-family: 'PingFang SC';
  font-size: 36px;
  text-align: right;
  margin-right: 30px;
}

.cardClass {
  margin-top: 30px;
}

.cardTitle {
  font-size: 24px;
  font-weight: bold;
  margin-top: 45px;
  margin-bottom: 30px;
}

.cardTitle2 {
  font-size: 20px;
  margin-left: 5px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-card {
  margin-left: 35px;
  margin-right: 35px;
}

.rowStyle {
  margin-left: 0px;
  margin-right: 0px;
  margin-top: 10px;
  margin-bottom: 40px;
}

.ml-2 {
  font-weight: 400;
}

.logo {
  text-align: left;
  font-family: 'PingFang SC';
  font-weight: bold;
  font-size: 20px;
  color: white;
}

.bottom {
  margin-left: 12px;
  margin-right: 12px;
  margin-top: 40px;
  margin-bottom: 15px;
  line-height: 12px;
  font-size: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}

.common-layout {
  margin: 0px;
  padding: 0px;
  border-top: 0px;
  height: auto;
  width: auto;
}

.common-layout .el-header {
  background-color: #20232c;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 60px;
}

.common-layout .el-footer {
  background-color: #20232c;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 60px;
}

.common-layout .el-aside {
  background-color: #20232c;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 200px;
}

.common-layout .el-main {
  background-color: #ffffff;
  color: var(--el-text-color-primary);
  text-align: center;
  padding: 0px;
  height: calc(100vh - 60px);
  /* line-height: 60px; */
}

.common-layout > .el-container {
  margin-bottom: 0px;
}

.common-layout .el-container:nth-child(5) .el-aside,
.common-layout .el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.common-layout .el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

a:link, a:visited {
  text-decoration: none;
  color: white;
}
a:hover {
  text-decoration: none;
  color: white;
}
a:active {
  text-decoration: none;
  color: white;
}

.imgHoverZoom {
  overflow: hidden;
  text-align: center;
}

.imgHoverZoom img {
  -webkit-transition: -webkit-transform .3s ease;
  -moz-transition: -moz-transform .3s ease;
  -ms-transition: -ms-transform .3s ease;
  transition: transform .3s ease;
}

.imgHoverZoom img:hover {
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  transform: scale(1.2);
}

.header {
  margin-left: 7px;
  width: 100%;
  height: 60px;
  background-color: rgba(255, 255, 255, 0);
  box-shadow: none;
  position: fixed;
  z-index: 999;
  transition: transform .2s ease;
}

</style>